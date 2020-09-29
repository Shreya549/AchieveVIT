from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .models import Feed
from Portfolio.models import Education, WorkExperience, Achievements
from Profile.models import FacultyProfile
from Accounts.models import Faculty
# Create your views here.

class ViewFeed(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            feed = Feed.objects.all().order_by('-timestamp')
            l = len(feed)
            ans = []
            # print (feed)
            for i in range(l):
                query = feed[i]
                type = query.type
                fk = query.fk
                # print(query)
                # print (type)
                if (type == 'Education'):
                    edu = Education.objects.get(pk=fk)
                    # print ("Edu")
                    owner = edu.owner
                    name = Faculty.objects.get(pk = owner).name
                    sub = name + " updated their Education."

                    json = {
                        "uuid" : query.uuid,
                        "Title" : sub,
                        "University" : edu.university,
                        "Degree" : edu.degree,
                        "From" : edu.start_year,
                        "To" : edu.end_year,
                        "Likes" : query.likes
                    }
                    # print (json)
                    ans.append(json)

                elif (type == 'Experience'):
                    edu = WorkExperience.objects.get(pk=fk)
                    # print(edu)
                    owner = edu.owner
                    name = Faculty.objects.get(pk = owner).name
                    sub = name + " updated their Work Experience."

                    json = {
                        "uuid" : query.uuid,
                        "Title" : sub,
                        "Position" : edu.position,
                        "Company" : edu.comp_name,
                        "Work description" : edu.description,
                        "period" : edu.period,
                        "Likes" : query.likes
                    }
                    # print (json)
                    ans.append(json)

                elif (type == 'Achievements'):
                    edu = Achievements.objects.get(pk=fk)
                    # print (edu)
                    owner = edu.owner
                    # print (owner)
                    name = Faculty.objects.get(pk = owner).name
                    sub = name + " added an Achievement."
                    # print (name)
                    json = {
                        "uuid" : query.uuid,
                        "Title" : sub,
                        "Details" : edu.details,
                        "Likes" : query.likes
                    }
                    # print (json)
                    ans.append(json)
                
            return Response({"feed" : ans}, status = 200)

        except:
            return Response({"feed" : "Error reaching Servers"}, status = 404)


class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        uuid = self.request.data["uuid"]
        feed = Feed.objects.get(pk = uuid)
        feed.likes += 1
        feed.save()
        return Response(status = 202)
         
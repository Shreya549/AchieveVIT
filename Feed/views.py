from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .models import Feed
from Portfolio.models import Education, WorkExperience, Achievements
from Profile.models import FacultyProfile

# Create your views here.
class ViewFeed(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            feed = Feed.objects.all().order_by('-timestamp')
            l = len(feed)
            ans = []
            print (feed)
            for i in range(l):
                query = feed[i]
                type = query.type
                fk = query.fk
                print(query)
                if (type == 'Education'):
                    edu = Education.objects.get(pk=fk)
                    print ("Edu")
                    owner = edu.owner
                    name = FacultyProfile.objects.get(pk = owner).name
                    sub = name + " updated their Education."

                    json = {
                        "Title" : sub,
                        "University" : edu.university,
                        "Degree" : edu.degree,
                        "From" : edu.start_year,
                        "To" : edu.end_year
                    }
                    print (json)
                    ans.append(json)

                elif (type == 'Experience'):
                    edu = WorkExperience.objects.get(pk=fk)

                    owner = edu.owner
                    name = FacultyProfile.objects.get(pk = owner).name
                    sub = name + " updated their Work Experience."

                    json = {
                        "Title" : sub,
                        "Position" : edu.position,
                        "Company" : edu.comp_name,
                        "Work description" : edu.description,
                        "period" : edu.period
                    }

                    ans.append(json)

                elif (type == 'Achievements'):
                    edu = Achievements.objects.get(pk=fk)

                    owner = edu.owner
                    name = FacultyProfile.objects.get(pk = owner).name
                    sub = name + " added an Achievement."

                    json = {
                        "Title" : sub,
                        "Details" : edu.description
                    }

                    ans.append(json)
                
            return Response({"feed" : ans}, status = 200)

        except:
            return Response({"feed" : "Error reaching Servers"}, status = 404)
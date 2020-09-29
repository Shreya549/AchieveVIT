from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import EducationViewSet, WorkExperienceViewSet, AchievementsViewSet, EducationRetrieveView, WorkExperienceRetrieveView, AchievementsRetrieveView

router = SimpleRouter()

router.register('education', EducationViewSet, basename="education")
router.register('experience', WorkExperienceViewSet, basename="experience")
router.register('achievements', AchievementsViewSet, basename="achievements")
router.register('viewEducation', EducationRetrieveView, basename = 'viewEducation')
router.register('viewExperience', WorkExperienceRetrieveView, basename = 'viewExperience')
router.register('viewAchievements', AchievementsRetrieveView, basename = 'viewAchievements')

urlpatterns = router.urls

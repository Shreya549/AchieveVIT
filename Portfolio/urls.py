from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import EducationViewSet, WorkExperienceViewSet, AchievementsViewSet

router = SimpleRouter()

router.register('education', EducationViewSet, basename="education")
router.register('experience', WorkExperienceViewSet, basename="experience")
router.register('achievements', AchievementsViewSet, basename="achievements")

urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FacultyProfileView, HRProfileView

router = SimpleRouter()

router.register('faculty', FacultyProfileView, basename="faculty")
router.register('hr', HRProfileView, basename="hr")

urlpatterns = router.urls

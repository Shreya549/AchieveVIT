from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FacultyProfileView, HRProfileView, ProfileRetrieveView

router = SimpleRouter()

router.register('faculty', FacultyProfileView, basename="faculty")
router.register('hr', HRProfileView, basename="hr")

urlpatterns = router.urls

urlpatterns +=[
    path('view/<int:pk>/', ProfileRetrieveView.as_view())
]
from django.urls import path, include
from .views import ViewFeed

urlpatterns = [
    path('view/', ViewFeed.as_view())
]

from django.urls import path, include
from .views import ViewFeed, LikeView

urlpatterns = [
    path('view/', ViewFeed.as_view()),
    path('like', LikeView.as_view())
]

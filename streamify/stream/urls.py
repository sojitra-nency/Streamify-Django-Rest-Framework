from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', UserChangePassword.as_view(), name='change-password'),
    path('send-password-reset-mail/', SendPasswordResetEmail.as_view(), name='sent-password-reset-,ail'),
    path('password-reset/<uid>/<token>/', PasswordResetView.as_view(), name='reset-password'),
    path('create-videos/', CreateVideo.as_view(), name='create-video'),
    path('video-detail/<pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('comments/<int:video_id>/', CommentListView.as_view(), name='comment-list'),
    path('list/', VideoListView.as_view(), name='list'),
    path('search/', SearchVideosView.as_view(), name='search'),
]

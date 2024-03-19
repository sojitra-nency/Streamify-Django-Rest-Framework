from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserRegistrationSerializer, LoginSerializer, UserProfileSerializer, ChangePasswordSerializer, PasswordResetSerializer, UserPasswordResetSerializer, CommentSerializer, VideoSerializer
from django.contrib.auth import authenticate
from stream.renderers import UserRenderer 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import generics
from django.utils import timezone
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

# Manually generate tokens for user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration successfull'}, status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    renderer_class = [UserRenderer]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login successfull'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePassword(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        
class SendPasswordResetEmail(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Email has been sent'}, status=status.HTTP_200_OK)

class PasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfull'}, status=status.HTTP_200_OK)

class CreateVideo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if 'publish_date' in serializer.validated_data:
            serializer.save(uploader=request.user)
        else:
            serializer.save(uploader=request.user, date_posted=timezone.now())
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VideoDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentListView(APIView):
    def get(self, request, video_id):
        comments = Comment.objects.filter(video_id=video_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, video_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, video_id=video_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OneVideoPerPagePagination(PageNumberPagination):
    page_size = 1

class VideoListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = OneVideoPerPagePagination
    
class SearchVideosView(APIView):
    permission_classes = [permissions.IsAuthenticated]  

    def get(self, request):
        search_term = request.query_params.get('search')  
        search_term = search_term[0:-1]
        
        if not search_term:
            return Response({'error': 'Missing search term'}, status=status.HTTP_400_BAD_REQUEST)

        filtered_videos = Video.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
        serializer = VideoSerializer(filtered_videos, many=True)
        return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Hackathon , HackathonParticipant, Submission
from .serializers import HackathonSerializer, HackathonParticipantSerializer, SubmissionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User

class HackathonEditPermission(BasePermission):

    message = 'You are not the owner of this hackathon.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user
    
class SubmissionEditPermission(BasePermission):
    
        message = 'You are not the owner of this submission.'
    
        def has_object_permission(self, request, view, obj):
            if request.method in SAFE_METHODS:
                return True
            return obj.user == request.user
    
class HackathonList(APIView):

    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        hackathons = Hackathon.objects.all()
        serializer = HackathonSerializer(hackathons, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HackathonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)
    
class HackathonDetails(APIView, HackathonEditPermission):

    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [HackathonEditPermission]

    def get(self, request, pk):
        try:
            hackathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = HackathonSerializer(hackathon)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            hadkathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serilaizer = HackathonSerializer(hadkathon, 
                                         data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        
        return Response(serilaizer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            hackathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        hackathon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HackathonParticipation(APIView):
    serializer_class = HackathonParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        try:
            hackathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        participants = HackathonParticipant.objects.filter(hackathon=hackathon)
        serializer = HackathonParticipantSerializer(participants, 
                                                    many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            hackathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user = self.request.user
        participate = HackathonParticipant(hackathon=hackathon, 
                                           user=user)
        participate.save()
        return Response(status=status.HTTP_201_CREATED)
        
class HackathonSubmissions(APIView,SubmissionEditPermission):

    serializer_class = SubmissionSerializer
    permission_classes = [SubmissionEditPermission]

    def get(self, request, pk):
        try:
            hackathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        submissions = Submission.objects.filter(hackathon=hackathon, 
                                                user=request.user)
        serializer = SubmissionSerializer(submissions, 
                                          many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        try:
            hackathon = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hackathon=hackathon, 
                            user=request.user)
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)
    
class UserHackathonList(APIView):
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        participating_hackathons = HackathonParticipant.objects.filter(user=request.user)
        hackathons = []
        for hackathon in participating_hackathons:
            hackathons.append(hackathon.hackathon)
        print(hackathons)
        serializer = HackathonSerializer(hackathons, 
                                         many=True)
        return Response(serializer.data)
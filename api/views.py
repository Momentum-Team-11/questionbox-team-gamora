from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer, UserSerializer, AnswerSerializer, QuestionAnswerSerializer
from .models import Question, Answer, User
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .custom_permissions import (
    IsAdminOrReadOnly,IsUserOrReadOnly
)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api_user_list', request=request, format=format),
        'question': reverse('api_question_list', request=request, format=format),
        'answer': reverse('api_answer_list', request=request, format=format)
    })



class QuestionViewSet(ModelViewSet): 
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsUserOrReadOnly]


class UserQuestionFavoritedViewSet(generics.ListCreateAPIView): 
    serializer_class = QuestionSerializer
    permission_classes = [IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Question.objects.exclude(favorited=None).filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserQuestionViewSet(generics.ListCreateAPIView): 
    serializer_class = QuestionSerializer
    permission_classes = [IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Question.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAnswerViewSet(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['answer']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Answer.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAnswerListSet(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['answer']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Answer.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAcceptedAnswerViewSet(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['answer']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Answer.objects.exclude(accepted=None).filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAcceptedFavoritedAnswerViewSet(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['answer']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Answer.objects.exclude(favorited=None).exclude(accepted=None).filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all().order_by("id")
    serializer_class = QuestionAnswerSerializer
    permission_classes = [IsUserOrReadOnly]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class AnswerViewSet(ListAPIView):
    queryset = Answer.objects.all().order_by("favorited")
    serializer_class = AnswerSerializer
    permission_classes = [IsUserOrReadOnly]


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsUserOrReadOnly]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsUserOrReadOnly]

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Question.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

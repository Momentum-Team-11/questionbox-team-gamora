from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer, UserSerializer, AnswerSerializer, QuestionAnswerSerializer
from .models import Question, Answer, User
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .custom_permissions import (
    IsAdminOrReadOnly,
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
    permission_classes = [IsAdminOrReadOnly]


class QuestionAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all().order_by("id")
	queryset2 = Answer.objects.all().order_by("favorited")
	serializer_class = QuestionAnswerSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class AnswerViewSet(ModelViewSet): 
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
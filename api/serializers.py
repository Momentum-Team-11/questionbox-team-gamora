from .models import Question, Answer, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        fields = ('id', 'username',)


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # favorited = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'user', 'question', 'favorited', 'created_at',)

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # favorited = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)

    class Meta:
        model = Answer
        fields = ('id', 'user', 'answer', 'questions', 'accepted', 'favorited', 'answered_at',)

class QuestionAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False, source='questions')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Question
        fields = ('id', 'user', 'question', 'answers')
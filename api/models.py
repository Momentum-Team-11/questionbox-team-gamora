from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=datetime.now)
    favorited = models.ManyToManyField(User, related_name="favorite_question")
    
    def __str__(self):
        return self.question

    def __repr__(self):
        return f"<Question: {self.question}>"


class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="answered", on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=datetime.now)
    favorited = models.ManyToManyField(User, related_name="favorite_answer")

    
    def __str__(self):
        return self.answer

    def __repr__(self):
        return f"<Answer: {self.answer}>"

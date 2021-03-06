"""question_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register("question", api_views.QuestionViewSet)
# router.register("answer", api_views.AnswerViewSet)
router.register("user", api_views.UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("api/auth/", include('djoser.urls')),
    path("api/auth/", include('djoser.urls.authtoken')),
    path('api/user_q_list', api_views.UserQuestionViewSet.as_view(), name='api_question_list'),
    path('api/user_favorited_q_list', api_views.UserQuestionFavoritedViewSet.as_view(), name='api_favorited_q_list'),
    path('api/question/<int:pk>/answers', api_views.QuestionAnswerDetail.as_view(), name='api_q_a_detail'),
    path('api/user_a_list', api_views.UserAnswerViewSet.as_view(), name='api_answer_list'),
    path('api/user_accepted_a_list', api_views.UserAcceptedAnswerViewSet.as_view(), name='api_accepted_a_list'),
    path('api/user_accepted_favorited_a_list', api_views.UserAcceptedFavoritedAnswerViewSet.as_view(), name='api_accepted_favorited_a_list'),
    path('api/answer', api_views.UserAnswerListSet.as_view(), name='api_answer'),
    path('api/answerviewset', api_views.AnswerViewSet.as_view(), name='api_answerviewset'),
    path('api/<int:pk>/answer_detail', api_views.AnswerDetail.as_view(), name='api_answer_detail'),
    path('api/<int:pk>/question_detail', api_views.QuestionDetail.as_view(), name='api_question_detail'),
    # path('users/', api_views.UserViewSet, name='api_user_list'),
    # path('api_root', api_views.api_root),
]




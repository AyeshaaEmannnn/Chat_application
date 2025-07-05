from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',SignupView.as_view(),name='SignUp'),
    path('login/',loginView.as_view(),name='LogIn'),
    # path('chat/',SendChatView.as_view(),name='send message'),
    path('chat/<int:user_id>/', ViewChatView.as_view(), name='chat'),
    #path('chatview/',ViewChatView.as_view(),name='view chat'), #/api/chat/?sender=1&receiver=2
    path('home/', homeView.as_view(), name='home')
]
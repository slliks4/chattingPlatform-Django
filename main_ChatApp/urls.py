from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('<int:id>/', views.Chat_box, name='chat_box'),
    path('sent/<int:id>/',views.Send_message, name="send_message")
]
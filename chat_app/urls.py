from django.urls import path
from .views import ChatListCreateView, ChatDetailView, GroupListCreateView, GroupDetailView
from .views import ReplyToMessageView
from .views import ReplyToMessageView
urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chat-list'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
    path('groups/', GroupListCreateView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('chats/<int:pk>/reply/', ReplyToMessageView.as_view(), name='reply-to-message'),
]




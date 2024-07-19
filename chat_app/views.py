from rest_framework import generics
from rest_framework.response import Response
from .models import Chat, Group
from .serializers import ChatSerializer, GroupSerializer

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            message = request.data.get('message')
            if message:
                instance.message = message  
                instance.save()  
                print(f"Received message: {message}")  
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


from rest_framework import generics
from rest_framework.response import Response
from .models import Chat
from .serializers import ChatSerializer
class ReplyToMessageView(generics.UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            reply_message = request.data.get('reply_message')
            if reply_message:
                instance.reply_message = reply_message
                instance.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

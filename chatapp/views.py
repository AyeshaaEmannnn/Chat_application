from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from django.shortcuts import redirect
# Create your views here.

class SignupView(APIView):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request,'login.html')
        return render(request,'signup.html')
    
class loginView(APIView):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            request.session['user_id'] = user.id  # ✅ Save session
            return redirect('home') 
        return render(request,'login.html')
    
class ViewChatView(APIView):

    def get(self, request, user_id):
        session_user_id = request.session.get('user_id')  # ✅ Get user from session
        if not session_user_id:
            return redirect('login')  # or return Response(..., 401)

        try:
            current_user = Signup.objects.get(id=session_user_id)
        except Signup.DoesNotExist:
            return redirect('login')

        other_user = Signup.objects.get(id=user_id)

        chats = Chat.objects.filter(
            sender_id__in=[current_user.id, other_user.id],
            receiver_id__in=[current_user.id, other_user.id]
        ).order_by('timestamp')

        return render(request, 'chat.html', {
            'messages': chats,
            'other_user': other_user,
            'user': current_user  # pass current user to template
        })

    def post(self, request, user_id):
        session_user_id = request.session.get('user_id')
        if not session_user_id:
            return redirect('login')

        try:
            current_user = Signup.objects.get(id=session_user_id)
        except Signup.DoesNotExist:
            return redirect('login')

        other_user = Signup.objects.get(id=user_id)
        message = request.POST.get('message')

        Chat.objects.create(sender=current_user, receiver=other_user, message=message)
        return redirect('chat', user_id=other_user.id)

class homeView(APIView):
    def get(self, request):
        user_id = request.session.get('user_id')  
        if not user_id:
            return redirect('login')

        try:
            current_user = Signup.objects.get(id=user_id)
        except Signup.DoesNotExist:
            return redirect('login')

        users = Signup.objects.exclude(id=current_user.id)  
        return render(request, 'home.html', {'user': current_user, 'users': users})



    
    
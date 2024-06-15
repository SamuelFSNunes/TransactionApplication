from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.models.modelUser import User
from api.repository.repository import Repository
from api.forms.loginForm import LoginForm
from api.auth.authentication import *

class LoginView(APIView):

    repository = Repository(User, 'users')

    def get(self, request):
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            auth = authenticate(email, password)
            
            if auth:
                token = generateToken(str(auth["_id"]), auth["email"])
                response = redirect("home")
                response.set_cookie("auth_token", token)
                return response
            else:
                form.add_error(None, 'Invalid credentials')
        return render(request, 'login/login.html', {'form': form})
    
class Logout(APIView):
    def get(self, request):
        response = redirect('home')
        response.delete_cookie('jwt')
        return response
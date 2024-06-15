from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User, UserSerializer
from api.repository.repository import Repository
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class UserView(APIView):
    model = User
    repository = Repository(model, 'users')

    authenticate = False
    user = None

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)
        print(error_code)

        if error_code == 0:
            user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=None):
        if not self.authenticate:
            return redirect("login")
        if id:
            user = self.repository.get_by_id(id)
            if user:
                serialized_user = UserSerializer(user)
                return render(request, 'user/user.html', {'users': serialized_user.data})
            else:
                return render(request, 'user/user.html', {'errors': f'{User.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = self.repository.get_all()
            serialized_users = UserSerializer(users, many=True)
            return render(request, 'user/user.html', {'users': serialized_users.data})
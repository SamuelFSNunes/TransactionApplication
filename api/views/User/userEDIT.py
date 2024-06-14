from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User, UserSerializer
from api.forms.userForm import UserForm
from api.repository.repository import Repository
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class UserEDIT(APIView):
    repository = Repository(User, 'users')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)
        print(error_code)

        if error_code == 0:
            user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        if not self.authenticate:
            return redirect("login")
        user = self.repository.get_by_id(id)
        userform = UserForm(initial=user.to_dict())
        return render(request, "user/userFormEdit.html", {"form": userform, "id": id})
    
    def post(self, request, id):
        if not self.authenticate:
            return redirect("login")
        userform = UserForm(request.POST)
        if userform.is_valid():
            serializer = UserSerializer(data=userform.cleaned_data)
            serializer.id = id
            if serializer.is_valid():
                self.repository.update(id, serializer.validated_data)
            else:
                print(serializer.errors)
        else:
            print(userform.errors)

        return redirect('users')
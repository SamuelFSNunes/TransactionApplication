from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User, UserSerializer
from api.forms.userForm import UserForm
from api.repository.repository import Repository
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class UserPOST(APIView):
    repository = Repository(User, 'users')

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

    def get(self, request):
        if not self.authenticate:
            return redirect("login")
        userform = UserForm()
        return render(request, "user/userForm.html", {"form": userform})
    
    def post(self, request):
        if not self.authenticate:
            return redirect("login")
        userform = UserForm(request.POST)
        if userform.is_valid():
            serializer = UserSerializer(data=userform.cleaned_data)
            if serializer.is_valid():
                self.repository.create(serializer.validated_data)
            else:
                return render(request, "user/userForm.html", {"form": userform, "errors": serializer.errors})
        else:
            return render(request, "user/userForm.html", {"form": userform, "errors": userform.errors})

        return redirect('users')
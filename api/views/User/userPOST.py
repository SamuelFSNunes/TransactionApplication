from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User, UserSerializer
from api.forms.userForm import UserForm
from api.repository.repository import Repository

class UserPOST(APIView):
    repository = Repository(User, 'users')

    def get(self, request):
        userform = UserForm()
        return render(request, "user/userForm.html", {"form": userform})
    
    def post(self, request):
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
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User, UserSerializer
from api.forms.userForm import UserForm
from api.repository.repository import Repository

class UserEDIT(APIView):
    repository = Repository(User, 'users')

    def get(self, request, id):
        user = self.repository.get_by_id(id)
        userform = UserForm(initial=user.to_dict())
        return render(request, "user/userFormEdit.html", {"form": userform, "id": id})
    
    def post(self, request, id):
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
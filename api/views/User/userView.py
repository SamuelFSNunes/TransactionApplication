from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User, UserSerializer
from api.repository.repository import Repository

class UserView(APIView):
    model = User
    repository = Repository(model, 'users')
    
    def get(self, request, id=None):
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
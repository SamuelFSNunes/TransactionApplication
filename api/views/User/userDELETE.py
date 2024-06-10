from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.userSerializer import User
from api.repository.repository import Repository

class UserDELETE(APIView):
    repository = Repository(User, 'users')

    def get(self, request, id=None):
        if not id:
            return render(request, 'user/user.html', {'errors': "ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        deleted = self.repository.delete(id)
        if deleted:
            return redirect("users")
        return render(request, 'user/user.html', {'errors': f'{User.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
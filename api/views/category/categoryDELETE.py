from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.categorySerializer import Category
from api.repository.repository import Repository

class categoryDELETE(APIView):
    repository = Repository(Category, 'categories')

    def get(self, request, id=None):
        if not id:
            return render(request, 'user/user.html', {'errors': "ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        deleted = self.repository.delete(id)
        if deleted:
            return redirect("categories")
        return render(request, 'user/user.html', {'errors': f'{Category.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
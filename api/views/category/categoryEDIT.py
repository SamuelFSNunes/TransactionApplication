from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.categorySerializer import Category, CategorySerializer
from api.repository.repository import Repository
from api.forms.categoryForm import CategoryForm
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class CategoryEDIT(APIView):
    repository = Repository(Category, 'categories')

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

    def get(self, request, id):
        if not self.authenticate:
            return redirect("login")
        if id:
            category = self.repository.get_by_id(id)
            if category:
                categoryForm = CategoryForm(initial=category.to_dict())
                return render(request, "category/categoryEditForm.html", {"form": categoryForm, "id": id})
            else:
               return render(request, "category/categoryEditForm.html", {"form": categoryForm, 'errors': f'{Category.__name__} not found'}, status=status.HTTP_404_NOT_FOUND) 
        else:
            return render(request, "category/categoryEditForm.html", {"form": categoryForm, "errors": "ID is required for edition"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, id):
        if not self.authenticate:
            return redirect("login")
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            serializer = CategorySerializer(data=categoryForm.cleaned_data)
            serializer.id = id
            if serializer.is_valid():
                self.repository.update(id, serializer.validated_data)
            else:
                return render(request, "category/categoryEditForm.html", {"form": categoryForm, "errors": serializer.errors})
        else:
            return render(request, "category/categoryEditForm.html", {"form": categoryForm, "errors": categoryForm.errors})
        return redirect('categories')
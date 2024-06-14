from typing import Any
from django.http import HttpRequest
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.auth.authentication import *
from api.serializers.categorySerializer import Category, CategorySerializer
from api.repository.repository import Repository

class CategoryView(APIView):
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

    def get(self, request, id=None):
        if not self.authenticate:
            return redirect("login")
        if id:
            category = self.repository.get_by_id(id)
            if category:
                serialized_category = CategorySerializer(category)
                return render(request, 'category/category.html', {"categories":serialized_category.data})
            else:
                return render(request, 'category/category.html', {'errors': f'{Category.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            categories = self.repository.get_all()
            serialized_categories = CategorySerializer(categories, many=True)
            return render(request, 'category/category.html', {"categories":serialized_categories.data})
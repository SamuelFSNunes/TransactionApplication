from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.categorySerializer import Category, CategorySerializer
from api.repository.repository import Repository

class CategoryView(APIView):
    repository = Repository(Category, 'categories')

    def get(self, request, id=None):
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
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.categorySerializer import Category, CategorySerializer
from api.repository.repository import Repository
from api.forms.categoryForm import CategoryForm

class CategoryEDIT(APIView):
    repository = Repository(Category, 'categories')


    def get(self, request, id):
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
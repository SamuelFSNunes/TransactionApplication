from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.categorySerializer import Category, CategorySerializer
from api.repository.repository import Repository
from api.forms.categoryForm import CategoryForm

class CategoryPOST(APIView):
    repository = Repository(Category, 'categories')


    def get(self, request):
        categoryForm = CategoryForm()
        return render(request, "category/categoryForm.html", {"form": categoryForm})
    
    def post(self, request):
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            serializer = CategorySerializer(data=categoryForm.cleaned_data)
            if serializer.is_valid():
                self.repository.create(serializer.validated_data)
            else:
                return render(request, "category/categoryForm.html", {"form": categoryForm, "errors": serializer.errors})
        else:
            return render(request, "category/categoryForm.html", {"form": categoryForm, "errors": categoryForm.errors})
        return redirect('categories')
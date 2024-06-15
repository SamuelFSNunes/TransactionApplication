from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.transactionSerializer import Transaction, CategorySerializer, TransactionSerializer
from api.serializers.categorySerializer import Category
from api.repository.repository import Repository
from api.forms.transactionForm import TransactionForm
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class TransactionPOST(APIView):

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
    
    def get(self, request):
        if not self.authenticate:
            return redirect("login")
        form = TransactionForm()
        return render(request, "transaction/transactionForm.html", {"form": form})
    
    def post(self, request):
        if not self.authenticate:
            return redirect("login")
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Obter os dados do formulário limpos
            cleaned_data = form.cleaned_data

            # Obter a categoria correspondente ao id fornecido
            category_repo = Repository(Category, 'categories')
            category = category_repo.get_by_id(cleaned_data['category']) # Mesma coisa que category_id

            # Atualizar os dados limpos com o ID da categoria
            cleaned_data['category'] = str(category.id) if category else None

            # Serializar os dados para validação
            serializer = TransactionSerializer(data=cleaned_data)

            # Criar a transação usando o repositório
            if serializer.is_valid():
                transaction_repo = Repository(Transaction, 'transactions')
                transaction_repo.create(serializer.data)

            # Redirecionar para uma página de sucesso ou lista de transações
            return redirect('transactions')
        else:
            return render(request, 'transaction/transactionForm.html', {"form": form, "errors": form.errors})
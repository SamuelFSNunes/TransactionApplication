from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.transactionSerializer import Transaction, TransactionSerializer
from api.repository.repository import Repository
from api.forms.transactionForm import TransactionForm
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class TransactionEDIT(APIView):
    repository = Repository(Transaction, 'transactions')

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
            transaction = self.repository.get_by_id(id)
            if transaction:
                transactionForm = TransactionForm(initial=transaction.to_dict())
                return render(request, "transaction/transactionForm.html", {"form": transactionForm, "id": id})
            else:
                return render(request, "transaction/transactionForm.html", {"form": transactionForm, 'errors': f'{Transaction.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return render(request, "transaction/transactionForm.html", {"form": transactionForm, 'errors': 'ID is required for edition'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        if not self.authenticate:
            return redirect("login")
        transactionForm = TransactionForm(request.POST)
        if transactionForm.is_valid():
            serializer = TransactionSerializer(data=transactionForm.cleaned_data)
            serializer.id = id
            if serializer.is_valid():
                self.repository.update(id, serializer.validated_data)
            else:
                return render(request, "transaction/transactionForm.html", {"form": transactionForm, 'errors': serializer.errors})
        else:
            return render(request, "transaction/transactionForm.html", {"form": transactionForm, 'errors': transactionForm.errors})
        return redirect('transactions')
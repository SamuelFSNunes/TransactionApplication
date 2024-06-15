from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.transactionSerializer import Transaction
from api.repository.repository import Repository
from typing import Any
from django.http import HttpRequest
from api.auth.authentication import *

class TransactionDELETE(APIView):
    repository = Repository(Transaction,'transactions')

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
        if not id:
            return render(request, 'transaction/transaction.html', {'errors': "ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            deleted = self.repository.delete(id)
        if deleted:
            return redirect('transactions')
        else:
            return render(request, 'transaction/transaction.html', {'errors': f'{Transaction.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)

from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.transactionSerializer import Transaction
from api.repository.repository import Repository

class TransactionDELETE(APIView):
    repository = Repository(Transaction,'transactions')

    def get(self, request, id=None):
        if not id:
            return render(request, 'transaction/transaction.html', {'errors': "ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            deleted = self.repository.delete(id)
        if deleted:
            return redirect('transactions')
        else:
            return render(request, 'transaction/transaction.html', {'errors': f'{Transaction.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)

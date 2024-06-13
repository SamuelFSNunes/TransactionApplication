from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.transactionSerializer import Transaction, TransactionSerializer
from api.repository.repository import Repository
from api.forms.transactionForm import TransactionForm

class TransactionEDIT(APIView):
    repository = Repository(Transaction, 'transactions')

    def get(self, request, id):
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
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.categorySerializer import Category, CategorySerializer
from api.serializers.transactionSerializer import Transaction, TransactionSerializer
from api.repository.repository import Repository
from datetime import datetime

class TransactionView(APIView):
    transaction_repository = Repository(Transaction, 'transactions')
    category_repository = Repository(Category, 'categories')
    category_serializer = CategorySerializer
    
    def get(self, request, id=None):
        if id:
            transaction = self.transaction_repository.get_by_id(id)
            if transaction:
                serializer = TransactionSerializer(transaction)
                # Formatar a data para DD-MM-YYYY
                formatted_data = self.format_data(serializer.data)
                category_id = formatted_data["category"]
                category = self.category_repository.get_by_id(category_id)
                return render(request, 'transaction/transaction.html', {'transactions': formatted_data, 'category': category})
            else:
                return render(request, 'transaction/transaction.html', {'errors': f'{Transaction.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            transactions = self.transaction_repository.get_all()
            serialized_transactions = TransactionSerializer(transactions, many=True)
            categories_dict = {}
            # Formatando todas as datas antes de enviar para o template
            formatted_transactions = [self.format_data(transaction_data) for transaction_data in serialized_transactions.data]

            for transaction_data in formatted_transactions:
                category_id = transaction_data["category"]
                if category_id not in categories_dict:
                    category = self.category_repository.get_by_id(category_id)
                    if category:
                        categories_dict[category_id] = category.name

            for transaction_data in formatted_transactions:
                category_id = transaction_data["category"]
                category_name = categories_dict.get(category_id)
                if category_name:
                    transaction_data["category_name"] = category_name

            return render(request, 'transaction/transaction.html', {'transactions': formatted_transactions})
        
    def format_data(self, data):
        # Verifica se existe a chave 'date' e formata se necessário
        if 'date' in data:
            try:
                # Tentar converter para datetime se for uma string
                data['date'] = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%Y')
            except ValueError:
                pass 
        return data
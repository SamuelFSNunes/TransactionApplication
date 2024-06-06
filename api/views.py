from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from api.repository.repository import Repository

class TestConnectionView(View):
    def get(self, request):
        repository = Repository()
        try:
            repository.db.command('ping')
            return JsonResponse({'message': 'Connection successful'}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Connection failed', 'error': str(e)}, status=500)

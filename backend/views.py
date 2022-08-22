from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def indexer(request):
    return JsonResponse({'status': ',success'})
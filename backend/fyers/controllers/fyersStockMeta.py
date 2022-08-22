from rest_framework.decorators import api_view
from ..business.fyersStockMetaBusiness import FyersStockMetaDataHandler
from django.http.response import JsonResponse
from rest_framework import status
import json

fyersStockMetaHandler = FyersStockMetaDataHandler()

@api_view(['GET'])
def GetMarketStatus(request):
    try:
        res = fyersStockMetaHandler.GetMarketStatus()
        response_data = {}
        if not (res is None):
            response_data['status'] = 'success'
            response_data['data'] = json.loads(res)
            return JsonResponse(response_data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'status':'failure', 'message' :'No Response'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        message = ''
        if hasattr(ex, 'message'):
            message = ex.message
        else:
            message = ex
        print(message)
        return JsonResponse({'status' : 'failure', 'message' : f'{message}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def RefreshStocksLList(request):
    try:
        fyersStockMetaHandler.RefreshStockList()
        return JsonResponse({'status':'success'}, status=status.HTTP_200_OK, safe=False)
    except Exception as ex:
        message = ''
        if hasattr(ex, 'message'):
            message = ex.message
        else:
            message = ex
        return JsonResponse({'status' : 'failure', 'message' : f'{message}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def GetStockList(request):
    try:
        stockKey = request.GET['StockKey']
        res = fyersStockMetaHandler.GetStockList(stockKey)
        response_data = {}
        if not (res is None):
            response_data['status'] = 'success'
            response_data['data'] = json.loads(res)
            return JsonResponse(response_data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'status':'failure', 'message' :'No Response'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        message = ''
        if hasattr(ex, 'message'):
            message = ex.message
        else:
            message = ex
        return JsonResponse({'status' : 'failure', 'message' : f'{message}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

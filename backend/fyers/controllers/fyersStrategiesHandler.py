from rest_framework.decorators import api_view
from ..business.fyersStrategiesBusiness import FyersStrategiesBusiness
from django.http.response import JsonResponse
from rest_framework import status
import json

fyersStrategiesHandler = FyersStrategiesBusiness()

@api_view(['GET'])
def StraddleOrder(request):
    try:
        #stockName = request.GET['StockSymbol']
        res = fyersStrategiesHandler.StreamStraddle("NSE:SBIN-EQ","NSE:SBIN-EQ", "NSE:SBIN-EQ", 5000, 'UP', 1, 'Buy', False)
        response_data = {}
        if not (res is None):
            response_data['status'] = 'success'
            response_data['data'] = json.loads(res.reset_index().to_json(orient='records'))
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
def GetActiveStrategies(request):
    try:
        #stockName = request.GET['StockSymbol']
        res = fyersStrategiesHandler.GetCurrentStrategies()
        response_data = {}
        if not (res is None):
            response_data['status'] = 'success'
            response_data['data'] = json.loads(res.reset_index().to_json(orient='records'))
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
def CancelStrategy(request):
    try:
        strategyId = request.GET['StrategyId']
        res = fyersStrategiesHandler.CancelStrategy(id=strategyId)
        response_data = {}
        if not (res is None):
            response_data['status'] = 'success'
            response_data['data'] = json.loads(res.reset_index().to_json(orient='records'))
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
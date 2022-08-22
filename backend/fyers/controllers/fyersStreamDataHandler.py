from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from ..business.fyersStreamDataBusiness import FyersStreamBusiness
import json, asyncio

fyersStream = FyersStreamBusiness()

@api_view(['GET'])
def StartStream(request):
    fyersStream.StartStream()
    return JsonResponse({'status' : 'success'},status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def AddStreamSymbol(request):
    stockName = request.GET['StockSymbol']
    fyersStream.AddSymbol(stockName)
    return JsonResponse({'status' : 'success'},status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def RemoveStreamSymbol(request):
    stockName = request.GET['StockSymbol']
    asyncio.run(fyersStream.RemoveSymbol(stockName))
    return JsonResponse({'status' : 'success'},status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def Stop(request):
    fyersStream.StopStream()
    return JsonResponse({'status' : 'success'},status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def RefreshStockData(request):
    fyersStream.RefreshStockData()
    return JsonResponse({'status' : 'success'},status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def GetData(request):
    try:
        stockKey = request.GET['StockKey']
        res = fyersStream.GetData(stockKey)
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
        return JsonResponse({'status' : 'failure', 'message' : f'{message}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
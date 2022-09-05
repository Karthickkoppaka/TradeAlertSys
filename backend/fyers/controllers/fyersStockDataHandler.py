from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from ..business.fyersStockDataBusiness import FyersStockDataBusiness

fyersStockDataBusiness = FyersStockDataBusiness()

@api_view(['GET'])
def GetStockLtp(request):
    try:
        stockName = request.GET['StockSymbol']
        fromDate = request.GET['FromDate']
        toDate = request.GET['ToDate']
        res = fyersStockDataBusiness.GetStockLtp(symbolTicker=stockName, fromDate=fromDate, toDate=toDate)
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
def GetStockListLtp(request):
    try:
        stockList = request.GET['StockSymbolList']
        fromDate = request.GET['FromDate']
        toDate = request.GET['ToDate']
        res = fyersStockDataBusiness.GetStockListLtp(symbolTicker=stockList, fromDate=fromDate, toDate=toDate)
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
def GetStockQuotes(request):
    try:
        stockName = request.GET['StockSymbol']
        res = fyersStockDataBusiness.GetStockQuotes(symbolTicker=stockName)
        print(res)
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
def GetStockMarketDepth(request):
    try:
        stockName = request.GET['StockSymbol']
        res = fyersStockDataBusiness.GetStockMarketDepth(symbolTicker=stockName)
        print(res)
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
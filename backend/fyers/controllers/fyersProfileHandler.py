import json
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from ..business.fyersUserBusiness import FyersUserBusiness
import json

fyersUserBusiness = FyersUserBusiness()

@api_view(['GET'])
def GetUserProfile(request):
    try:
        res = fyersUserBusiness.GetUserProfile()
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
def GetFundProfile(request):
    try: 
        res = fyersUserBusiness.GetUserFundDetails()
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

@api_view(['GET'])
def GetHoldingProfile(request):
    try: 
        res = fyersUserBusiness.GetUserHoldingsDetails()
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
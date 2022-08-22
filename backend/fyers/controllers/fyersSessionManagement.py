from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from django.http.response import JsonResponse

from ...config import FrontEnd
from ..business.fyersSessionBusiness import FyersSessionBusiness

fyersSessionBusiness = FyersSessionBusiness()

@api_view(['GET'])
def FyersLogin(request):
    print('Fyers_Login called')
    return redirect(fyersSessionBusiness.authURL)


@api_view(['GET','POST'])
def FyersPostLogin(request):
    res_auth_code = request.GET['auth_code']
    global fyersSessionBusiness
    fyersSessionBusiness.update_parameters(res_auth_code)
    return redirect(FrontEnd.post_login_url)


@api_view(['GET'])
def FyersStatus(request):
    global fyersSessionBusiness
    if fyersSessionBusiness.access_token is None or fyersSessionBusiness.access_token == '':
        return JsonResponse({'status' : 'failure'}, status=status.HTTP_400_BAD_REQUEST)
    if fyersSessionBusiness.fyers_session_model is None or fyersSessionBusiness.fyers_session_model == '':
        return JsonResponse({'status' : 'failure'}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'status' : 'success', 'authToken' : fyersSessionBusiness.auth_token, 'accessToken' : fyersSessionBusiness.access_token }, status=status.HTTP_200_OK)


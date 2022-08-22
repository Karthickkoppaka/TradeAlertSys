from fyers_api import fyersModel, accessToken
from ...config import FyersParameters

configParam = FyersParameters()

class FyersSessionBusiness():
    #fyers_session_model = fyersModel.FyersModel(client_id=configParam.app_id, token='', log_path='fv2/')
    fyers_session_model = fyersModel.FyersModel(client_id=configParam.app_id, token='', log_path='')
    #Parameters
    auth_token = ''
    access_token = ''
    sessoin = ''
    authURL = ''

    def __init__(self):
        self.app_id = configParam.app_id
        self.secret_id = configParam.secret_id
        self.redirectUrl = configParam.rediect_url
        self.response_type = 'code'
        self.grant_type = 'authorization_code'
        FyersSessionBusiness.Update_Session(self.app_id, self.secret_id, self.redirectUrl, self.response_type, self.grant_type)
        FyersSessionBusiness.get_authUrl()

    @classmethod
    def Update_Session(cls, appId, secretId, redirectUri, responseType, grantType):
        cls.sessoin = accessToken.SessionModel(
            client_id = appId,
            secret_key = secretId,
            redirect_uri=redirectUri,
            response_type=responseType,
            grant_type=grantType
        )
    
    @classmethod
    def get_authUrl(cls):
        cls.authURL = cls.sessoin.generate_authcode()

    @classmethod
    def set_authcode(cls, value):
        cls.sessoin.set_token(value)
        response = cls.sessoin.generate_token()
        #print(f'response {response}')
        if response['s'] == 'ok':
            access_token = response['access_token']
        else:
            access_token = ''
        
        return access_token

    def update_parameters(self, auth_token_val):
        FyersSessionBusiness.update_auth_token(auth_token_val)
    
    def GenerateAccessToken(self):
        pass
        
    
    @classmethod
    def update_auth_token(cls, value):
        cls.auth_token = value
        cls.access_token = FyersSessionBusiness.set_authcode(value)
        cls.fyers_session_model = fyersModel.FyersModel(client_id=configParam.app_id, token=cls.access_token, log_path='fv2/')
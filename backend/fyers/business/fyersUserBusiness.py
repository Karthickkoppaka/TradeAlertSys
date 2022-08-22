from .fyersSessionBusiness import FyersSessionBusiness
import json

fyersSession = FyersSessionBusiness()

class FyersUserBusiness():

    def GetUserProfile(self):
        global fyersSession
        res = fyersSession.fyers_session_model.get_profile()
        if(self.GetResponseStatus(res)):
            jres = json.loads(json.dumps(res['data']))
            #print(jres)
            #print(type(jres))
            return jres
    
    def GetUserFundDetails(self):
        global fyersSession
        res = fyersSession.fyers_session_model.funds()
        if(self.GetResponseStatus(res)):
            jres = json.loads(json.dumps(res['fund_limit']))
            print(jres)
            return jres

    def GetUserHoldingsDetails(self):
        global fyersSession
        res = fyersSession.fyers_session_model.holdings()
        print(res)
        if(self.GetResponseStatus(res)):
            jres = json.loads(json.dumps(res['holdings']))
            return jres
    
    def GetResponseStatus(self, result):
        if (result['s'] == 'ok'):
            return True
        else:
            return False
    
    def GetFyersStatus(self):
        global fyersSession
        res = fyersSession.fyers_session_model

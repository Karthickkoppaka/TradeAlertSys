from .fyersSessionBusiness import FyersSessionBusiness
import pandas as pd
import datetime, pytz, json

fyersSession = FyersSessionBusiness()

class FyersStockDataBusiness():

    def GetStockLtp(self, symbolTicker, fromDate, toDate):
        global fyersSession
        data = {"symbol":symbolTicker,"resolution":"D","date_format":"1","range_from":fromDate,"range_to":toDate,"cont_flag":"1"}
        retdata= fyersSession.fyers_session_model.history(data)['candles']
        rdata = pd.DataFrame(retdata, columns=['ETime', 'Open', 'High', 'Low', 'Close', 'Volume'])
        tz = pytz.timezone('Asia/Kolkata')
        rdata['Time'] = rdata['ETime'].apply(lambda x: str(datetime.datetime.fromtimestamp(x)))
        rdata['Symbol'] = symbolTicker
        print(f'GetStockLtp {rdata}')
        return rdata

    def GetStockQuotes(self, symbolTicker):
        global fyersSession
        data = {"symbols":symbolTicker}
        colNames = ['Symbol','Ltp','ask','bid', 'Time', 'ETime', 'Open', 'High', 'Low', 'Close', 'Volume']
        res = fyersSession.fyers_session_model.quotes(data)
        if(self.GetResponseStatus(res)):
            dt = pd.json_normalize(res,record_path=['d'])
            jdata = dt[['v.symbol','v.lp','v.ask','v.bid','v.cmd.tf','v.cmd.t','v.cmd.o','v.cmd.h','v.cmd.l','v.cmd.c','v.cmd.v']]
            jdata.columns = colNames
            return jdata
    
    
    def GetStockMarketDepth(self, symbolTicker):
        global fyersSession
        data = {"symbol":symbolTicker, "ohlcv_flag":"1"}
        print(f'data {data}')
        colNames = ['Symbol','Ltp','ask','bid', 'Time', 'ETime', 'Open', 'High', 'Low', 'Close', 'Volume']
        res = fyersSession.fyers_session_model.depth(data)
        if(self.GetResponseStatus(res)):
            dbid = pd.DataFrame(res["d"][f"{symbolTicker}"]["bids"])
            dbid['Type'] = 'Bid'
            dask = pd.DataFrame(res["d"][f"{symbolTicker}"]["bids"])
            dask['Type'] = 'Ask'
            data = pd.concat([dbid, dask], ignore_index=True)
            print(f'data {data.to_json(orient="records")}')
            return data

    def GetResponseStatus(self, result):
        if (result['s'] == 'ok'):
            return True
        else:
            return False




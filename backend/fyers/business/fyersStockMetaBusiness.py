from dataclasses import fields
from datetime import datetime, timezone
from django.core import serializers
from .fyersSessionBusiness import FyersSessionBusiness
import json
import pytz
import pandas as pd
from ...config import FyersParameters
from ..fyersModels import FyersStockList

fyersSession = FyersSessionBusiness()
fyersParameters = FyersParameters()

class FyersStockMetaDataHandler():
    symbolColumns = ['Fytoken','SymbolDetails','ExchangeInstrumentType','MinimumLotSize','TickSize','ISIN','TradingSession','LastUpdateDate','ExpiryDate','SymbolTicker','Exchange','Segment','ScripCode','MainStockName','UnderlyingScripCode','StrikePrice','OptionType']    
    def GetMarketStatus(self):
        global fyersSession
        res = fyersSession.fyers_session_model.market_status()
        if(self.GetResponseStatus(res)):
            jres = json.loads(json.dumps(res['marketStatus']))
            return jres

    def GetResponseStatus(self, result):
        if (result['s'] == 'ok'):
            return True
        else:
            return False

    def RefreshStockList(self):
        res = pd.read_csv(fyersParameters.symbol_nse_capital_url)
        res.columns = self.symbolColumns
        self.StockEntityModelMapper(res)
        res = pd.read_csv(fyersParameters.symbol_nse_currency_url)
        res.columns = self.symbolColumns
        self.StockEntityModelMapper(res)
        res = pd.read_csv(fyersParameters.symbol_nse_equity_url)
        res.columns = self.symbolColumns
        self.StockEntityModelMapper(res)
        res = pd.read_csv(fyersParameters.symbol_bse_capital_url)
        res.columns = self.symbolColumns
        self.StockEntityModelMapper(res)
        res = pd.read_csv(fyersParameters.symbol_commodity_url)
        res.columns = self.symbolColumns
        self.StockEntityModelMapper(res)
        #print(res.head(10))
        print('count')
        print(FyersStockList.objects.count())

    def StockEntityModelMapper(self, data):
        data.reset_index()
        modelItems = []
        for id in data.index:
            print(id)
            modelList = FyersStockList()
            modelList.Fytoken =  int(data['Fytoken'][id])
            modelList.SymbolDetails =  data['SymbolDetails'][id]
            modelList.ExchangeInstrumentType =  int(data['ExchangeInstrumentType'][id])
            modelList.MinimumLotSize =  int(data['MinimumLotSize'][id])
            modelList.TickSize =  float(data['TickSize'][id])
            modelList.ISIN =  data['ISIN'][id]
            modelList.TradingSession =  data['TradingSession'][id]
            modelList.LastUpdateDate =  str(data['LastUpdateDate'][id])
            modelList.ExpiryDate =  data['ExpiryDate'][id]
            modelList.SymbolTicker =  data['SymbolTicker'][id]
            modelList.Exchange =  int(data['Exchange'][id])
            modelList.Segment =  int(data['Segment'][id])
            modelList.ScripCode =  int(data['ScripCode'][id])
            modelList.UnderlyingScripCode =  int(data['UnderlyingScripCode'][id])
            modelList.MainStockName =  data['MainStockName'][id]
            modelList.StrikePrice = float(data['StrikePrice'][id])
            modelList.OptionType =  data['OptionType'][id]
            modelList.date_added =  datetime.now(pytz.UTC)
            #modelList.save()
            modelItems.append(modelList)
        
        FyersStockList.objects.bulk_create(modelItems)
    
    def GetStockList(self, stockKey):
        print(stockKey)
        data = FyersStockList.objects.filter(SymbolDetails__icontains =stockKey).values('SymbolDetails','SymbolTicker')
        return list(data)

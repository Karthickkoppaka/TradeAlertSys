from datetime import datetime, timedelta
from .fyersStreamDataBusiness import FyersStreamBusiness, streamColumns, streamDepthColumns
from .fyersStockDataBusiness import FyersStockDataBusiness
from .fyersOrdersBusiness import FyersOrderManagementBusiness
from ..fyersConstants import BuyorSellSide
import random as rd
from time import time, sleep
import pandas as pd
import requests, asyncio

fyersStream = FyersStreamBusiness()
fyersOrderManagment = FyersOrderManagementBusiness()
fyersStockDataHandler = FyersStockDataBusiness()

#DataStores
col = ['Strategy', 'Id', 'Symbol', 'OrderTimeStamp', 'OrderId', 'TriggerPrice', 'OrderStatus']
fyersStategiesOrders = pd.DataFrame(columns=col)
colEnq = ['Id', 'Strategy', 'TargetSymbol', 'EnquieTimeStamp', 'TriggerPrice', 'CurrentPrice','QueueStatus', 'TargetOptionCE', 'TargetOptionPE' ]
fyersStategiesEnque = pd.DataFrame(columns=colEnq)

class FyersStrategiesBusiness():

    def __init__(self) -> None:
        pass

    def StreamStraddle(self, optionLevelCE, optionLevelPE, stockTargetSymbol,stockTargetLevel, direction, quantity, buyOrSell, isStream=False):
        global fyersStream, fyersOrderManagment, fyersStategiesOrders, fyersStategiesEnque, colEnq
        isLevelReached = False
        enqId = rd.randint(0,999999)
        enqueData = [enqId, 'Straddle', stockTargetSymbol, datetime.utcnow(), stockTargetLevel, '', 'Pending', optionLevelCE, optionLevelPE]
        if fyersStategiesEnque.empty:
            fyersStategiesEnque = pd.DataFrame([enqueData], columns=colEnq)
        else:
            fyersStategiesEnque = pd.concat([fyersStategiesEnque, pd.DataFrame([enqueData], columns=colEnq)], ignore_index=True, sort=False)
        
        #print(f'fyersStategiesEnque {fyersStategiesEnque}')
        if isStream:
            print('call addsymbol')
            #fyersStream.AddSymbol(stockTargetSymbol)
            try:
                requests.get(f'http://127.0.0.1:8000/api/Fyers/Stream/Add?StockSymbol={stockTargetSymbol}',timeout=0.0000000001)
            except requests.exceptions.ReadTimeout:
                pass

        while not isLevelReached:
            print('Looop')
            data = pd.DataFrame(columns = streamColumns)
            if isStream:
                data = fyersStream.GetData('Stock')
            else:
                data = self.GetStockData(stockTargetSymbol)
            data = data.tail(1).reset_index()
            #print(f'main1 data {data}')
            triggerlevel= pd.DataFrame(streamColumns)
            #dataDepth = fyersStream.GetData('StockDepth')
            triggerlevel = data[data['symbol']==stockTargetSymbol]
            #print(f'triggerlevel {triggerlevel}')
            if (direction == 'UP'):
                triggerlevel = data[data['ltp']>stockTargetLevel]
            elif (direction == 'DOWN'):
                triggerlevel = data[data['ltp']<stockTargetLevel]
                
            if not triggerlevel.empty:
                isLevelReached = True
                print('level reached')
                #ordertype = BuyorSellSide.Buy.value if buyOrSell == 'Buy' else (BuyorSellSide.Sell.value if buyOrSell == 'Sell' else '')
                ceOrder = fyersOrderManagment.MarketOrder(optionLevelCE, quantity, buyOrSell)
                peOrder = fyersOrderManagment.MarketOrder(optionLevelPE, quantity, buyOrSell)
                print(f'ceOrder {ceOrder}')
                print(f'peOrder {peOrder}')
                #print(f"peOrder {ceOrder['s'] != 'ok' and peOrder['s'] == 'ok'}")
                if ceOrder['s'] != 'ok' and peOrder['s'] == 'ok':
                    fyersOrderManagment.CancelOrder(peOrder['id'])
                    fyersStategiesEnque.loc[(fyersStategiesEnque.Id == enqId) & (fyersStategiesEnque.Strategy == 'Straddle'), 'QueueStatus'] = 'Failed'
                elif peOrder['s'] != 'ok' and ceOrder['s'] == 'ok':
                    fyersOrderManagment.CancelOrder(ceOrder['id'])
                    fyersStategiesEnque.loc[(fyersStategiesEnque.Id == enqId) & (fyersStategiesEnque.Strategy == 'Straddle'), 'QueueStatus'] = 'Failed'
                elif peOrder['s'] == 'ok' and ceOrder['s'] == 'ok':
                    ceOrderDetails = ['Straddle', enqId, optionLevelCE, datetime.utcnow(), ceOrder['id'], '', 'Placed']
                    pd.concat([fyersStategiesOrders,pd.DataFrame([ceOrderDetails])], ignore_index=True, sort=False)
                    peOrderDetails = ['Straddle', enqId, optionLevelPE, datetime.utcnow(), peOrder['id'], '', 'Placed']
                    pd.concat([fyersStategiesOrders,pd.DataFrame([peOrderDetails])], ignore_index=True, sort=False)
                    fyersStategiesEnque.loc[(fyersStategiesEnque.Id == enqId) & (fyersStategiesEnque.Strategy == 'Straddle'), 'QueueStatus'] = 'Completed'
                else:
                    print('else')
                    fyersStategiesEnque.loc[(fyersStategiesEnque.Id == enqId) & (fyersStategiesEnque.Strategy == 'Straddle'), 'QueueStatus'] = 'Failed'
            else:
                if not data.empty:
                    #print(f'data12 {data["ltp"][0]}')
                    fyersStategiesEnque.loc[(fyersStategiesEnque.Id == enqId) & (fyersStategiesEnque.Strategy == 'Straddle'), 'CurrentPrice'] = data['ltp']
                fyersStategiesEnque.loc[(fyersStategiesEnque.Id == enqId) & (fyersStategiesEnque.Strategy == 'Straddle'), 'EnquieTimeStamp'] = datetime.utcnow()
                #print(f'fyersStategiesEnque else {fyersStategiesEnque}')
                #sleep(60 - time() % 60)
                sleep(10)

            print(f'fyersStategiesEnque {fyersStategiesEnque}')
            
        return fyersStategiesEnque
            
    def GetCurrentStrategies(self):
        global fyersStategiesEnque
        return fyersStategiesEnque

    def CancelStrategy(self, id):
        global fyersStategiesEnque
        print(f'CancelStrategy id {id}')
        print(f'CancelStrategy Before {fyersStategiesEnque}')
        fyersStategiesEnque = fyersStategiesEnque[fyersStategiesEnque['Id'] != id]
        print(f'CancelStrategy After {fyersStategiesEnque}')
        return fyersStategiesEnque
    
    def GetStockData(self, symbol):
        fromDate = (datetime.today()- timedelta(days=5)).strftime('%Y-%m-%d')
        toDate = datetime.today().strftime('%Y-%m-%d')
        response = fyersStockDataHandler.GetStockLtp(symbolTicker=symbol, fromDate=fromDate, toDate=toDate)
        input = [symbol, datetime.today().strftime('%Y-%m-%d %H:%M:%S'), response['Close'][0]]
        # print(f'input {input}')
        data = pd.DataFrame([input], columns=['symbol', 'timestamp', 'ltp'])
        #print(f'data {data}')
        return data

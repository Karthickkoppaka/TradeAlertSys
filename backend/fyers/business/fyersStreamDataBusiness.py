import asyncio
import os, json, sys
from datetime import datetime
import pytz
from tracemalloc import stop
from ...config import FyersParameters
from .fyersSessionBusiness import FyersSessionBusiness
from ..fyersModels import FyersStockTracker, FyersStockDepthTracker
from fyers_api.websocket import ws
from fyers_api.websocket.ws import FyersSocket
import pandas as pd

fyersConfig = FyersParameters()
fyersSession = FyersSessionBusiness()

# Log Location
dir = os.path.abspath(os.path.dirname(__file__))
dir = dir[:dir.rfind('\\')]
dir = dir[:dir.rfind('\\')]
logdir = os.path.join(dir, 'logs')
out_path = os.path.join(logdir,'out.csv')
logdir = os.path.join(dir, 'logs').replace('\\','/')

# DataStore
columnProfile = ['symbol', 'timestamp','ltp', 'Open', 'High', 'Low', 'Close']
dataStore = pd.DataFrame(columns = columnProfile)
stickDataStore = pd.DataFrame(columns = columnProfile)

streamColumns = ['symbol', 'timestamp', 'fyCode', 'fyFlag', 'pktLen', 'ltp',
       'open_price', 'high_price', 'low_price', 'close_price',
       'min_open_price', 'min_high_price', 'min_low_price', 'min_close_price',
       'min_volume', 'last_traded_qty', 'last_traded_time', 'avg_trade_price',
       'vol_traded_today', 'tot_buy_qty', 'tot_sell_qty']
streamDepthColumns = ['symbol', 'fyCode', 'ltp', 'price', 'qty', 'num_orders']
streamData = pd.DataFrame(columns = streamColumns)
streamDepthData = pd.DataFrame(columns = streamDepthColumns)

#TrackSybmols
trackSymbols = []
# DataStore
columnProfile = ['symbol', 'timestamp','ltp', 'day_open', 'day_high', 'day_low', 'day_close']
dataStore = pd.DataFrame(columns = columnProfile)
stickDataStore = pd.DataFrame(columns = columnProfile)

#fyers_socket = ws.FyersSocket(access_token=accessToken, data_type= 'symbolData')
stopFlag = False
i = 1
def FyersSocketListener(self):
        global streamData, streamDepthData, streamColumns
        global i, stopFlag
        message = self.response
        #print (f"Custom:{str(message)}")
        #print (f"Custom:{type(message)}") #<class 'list'>
        if len(message) > 0:
            #message="[{'symbol': 'NSE:SBIN-EQ', 'timestamp': 1658394515, 'fyCode': 7208, 'fyFlag': 2, 'pktLen': 200, 'ltp': 512.3, 'open_price': 509.8, 'high_price': 513.4, 'low_price': 506.75, 'close_price': 508.6, 'min_open_price': 512.5, 'min_high_price': 512.6, 'min_low_price': 512.3, 'min_close_price': 512.3, 'min_volume': 14444, 'last_traded_qty': 39, 'last_traded_time': 1658394515, 'avg_trade_price': 51133, 'vol_traded_today': 10748355, 'tot_buy_qty': 802405, 'tot_sell_qty': 1620615, 'market_pic': [{'price': 512.29, 'qty': 863, 'num_orders': 8}, {'price': 512.25, 'qty': 544, 'num_orders': 2}, {'price': 512.2, 'qty': 692, 'num_orders': 5}, {'price': 512.15, 'qty': 4500, 'num_orders': 12}, {'price': 512.1, 'qty': 1280, 'num_orders': 12}, {'price': 512.35, 'qty': 46, 'num_orders': 1}, {'price': 512.4, 'qty': 1455, 'num_orders': 1}, {'price': 512.45, 'qty': 3305, 'num_orders': 12}, {'price': 512.5, 'qty': 738, 'num_orders': 10}, {'price': 512.54, 'qty': 13455, 'num_orders': 19}]}]"
            inStr = str(message).replace("'", '"')
            data = json.loads(inStr)
            dr = pd.DataFrame(data, columns=streamColumns)
            mk = pd.DataFrame(data[0]['market_pic'])
            mk['symbol'] = dr['symbol'][0]
            mk['fyCode'] = dr['fyCode'][0]
            mk['ltp'] = dr['ltp'][0]
            mk['timestamp'] = dr['timestamp'][0]
            streamData = pd.concat([streamData, dr], ignore_index=True)
            streamDepthData = pd.concat([streamDepthData, mk], ignore_index=True)
            
        i = i + 1
        #print(f'i {i}')
        if stopFlag:
            print('stopFlag')
            asyncio.get_event_loop().stop()
        

FyersSocket.websocket_data = FyersSocketListener

class FyersStreamBusiness():

    def __init__(self):
        self.i = 1
        self.fyers_socket = ''
    
    def CreateSocket(self):
        ws.websocket = FyersSocketListener

    async def StartStream(self):
        global fyersConfig
        data_type = "symbolData"
        symbol = ["NSE:SBIN-EQ"]
        accessToken = f'{fyersConfig.app_id}:{fyersSession.access_token}'
        fs = FyersSocket(access_token=accessToken, data_type=data_type,symbol=symbol)
        asyncio.set_event_loop(asyncio.new_event_loop())
        fs.subscribe()

    def AddSymbol(self, symbol):
        global fyersConfig, trackSymbols
        print('AddSymbol')
        data_type = "symbolData"
        #symbol = "NSE:SBIN-EQ"
        if not len(trackSymbols):
            trackSymbols = [f"{symbol}"]
        else:
            trackSymbols.append([f"{symbol}"])
        print(f'trackSymbols {trackSymbols}')
        accessToken = f'{fyersConfig.app_id}:{fyersSession.access_token}'
        fs = FyersSocket(access_token=accessToken, data_type=data_type,symbol=trackSymbols)
        asyncio.set_event_loop(asyncio.new_event_loop())
        fs.subscribe()
    
    async def RemoveSymbol(self, symbol):
        global fyersConfig
        data_type = "symbolData"
        symbol = "NSE:SBIN-EQ"
        trackSymbols.remove([f"{symbol}"])
        accessToken = f'{fyersConfig.app_id}:{fyersSession.access_token}'
        fs = FyersSocket(access_token=accessToken, data_type=data_type,symbol=trackSymbols)
        asyncio.set_event_loop(asyncio.new_event_loop())
        fs.subscribe()

    def StopStream(self):
        data_type = "symbolData"
        symbol = ["NSE:SBIN-EQ", "NSE:SETFNIF50-EQ"]
        #fs = FyersSocket(access_token=accessToken, data_type=data_type,symbol=symbol)
        #fs.unsubscribe(symbol=symbol)
        #asyncio.get_event_loop().stop() 
        #print(asyncio.get_event_loop())
        global stopFlag
        stopFlag = True
    
    def GetData(self, param):
        global streamData, streamDepthData
        if param == 'Stock':
            return streamData
        elif param == 'StockDepth':
            return streamDepthData
        

    def RefreshStockData(self):
        global streamData, streamDepthData
        FyersStockTracker.objects.filter(date_added__date=datetime.now().date()).delete()
        self.FyersStockTrackerMapper(streamData)
        FyersStockDepthTracker.objects.filter(date_added__date=datetime.now().date()).delete()
        self.FyersStockDepthTrackerMapper(streamDepthData)

    def FyersStockTrackerMapper(self, data):
        data.reset_index()
        modelItems = []
        for id in data.index:
            modelList = FyersStockTracker()
            modelList.symbol = data['symbol'][id]
            modelList.timestamp = int(data['timestamp'][id])
            modelList.fyCode = int(data['fyCode'][id])
            modelList.fyFlag = int(data['fyFlag'][id])
            modelList.pktLen = int(data['pktLen'][id])
            modelList.ltp = float(data['ltp'][id])
            modelList.open_price = float(data['open_price'][id])
            modelList.high_price = float(data['high_price'][id])
            modelList.low_price = float(data['low_price'][id])
            modelList.close_price = float(data['close_price'][id])
            modelList.min_open_price = float(data['min_open_price'][id])
            modelList.min_high_price = float(data['min_high_price'][id])
            modelList.min_low_price = float(data['min_low_price'][id])
            modelList.min_close_price = float(data['min_close_price'][id])
            modelList.min_volume = int(data['min_volume'][id])
            modelList.last_traded_qty = int(data['last_traded_qty'][id])
            modelList.last_traded_time = int(data['last_traded_time'][id])
            modelList.avg_trade_price = float(data['avg_trade_price'][id])
            modelList.vol_traded_today = int(data['vol_traded_today'][id])
            modelList.tot_buy_qty = int(data['tot_buy_qty'][id])
            modelList.tot_sell_qty = int(data['tot_sell_qty'][id])
            modelList.date_added = datetime.now(pytz.UTC)
            modelItems.append(modelList)
        
        FyersStockTracker.objects.bulk_create(modelItems)

    def FyersStockDepthTrackerMapper(self, data):
        data.reset_index()
        modelItems = []
        for id in data.index:
            modelList = FyersStockDepthTracker()
            modelList.symbol = data['symbol'][id]
            modelList.fyCode = int(data['fyCode'][id])
            modelList.timestamp = int(data['timestamp'][id])
            modelList.ltp = float(data['ltp'][id])
            modelList.price = float(data['price'][id])
            modelList.qty = int(data['qty'][id])
            modelList.num_orders = int(data['num_orders'][id])
            modelList.date_added = datetime.now(pytz.UTC)
            modelItems.append(modelList)
        
        FyersStockDepthTracker.objects.bulk_create(modelItems)
    
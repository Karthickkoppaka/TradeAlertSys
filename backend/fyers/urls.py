#To Define routes
from django.urls import path
from django.urls.conf import include
from .controllers import fyersSessionManagement, fyersProfileHandler, fyersStockMeta, fyersStockDataHandler, fyersStreamDataHandler, fyersStrategiesHandler

urlpatterns = [
    #Login Fyers Session
    path('Login', fyersSessionManagement.FyersLogin),
    path('PostLogin', fyersSessionManagement.FyersPostLogin),
    path('Status', fyersSessionManagement.FyersStatus),
    #Fyers User Profile
    path('User/UserProfile', fyersProfileHandler.GetUserProfile),
    path('User/FundProfile', fyersProfileHandler.GetFundProfile),
    path('User/HoldingProfile', fyersProfileHandler.GetHoldingProfile),
    #StockMeta
    path('Stock/MarketStatus', fyersStockMeta.GetMarketStatus),
    path('Stock/StockListRefresh', fyersStockMeta.RefreshStocksLList),
    path('Stock/StockList', fyersStockMeta.GetStockList),
    #StockData
    path('StockData/Ltp', fyersStockDataHandler.GetStockLtp),
    path('StockData/Quotes', fyersStockDataHandler.GetStockQuotes),
    path('StockData/MarketDepth', fyersStockDataHandler.GetStockMarketDepth),
    #Stream
    path('Stream/Start', fyersStreamDataHandler.StartStream),
    path('Stream/Add', fyersStreamDataHandler.AddStreamSymbol),
    path('Stream/Stop', fyersStreamDataHandler.Stop),
    path('Stream/Refresh', fyersStreamDataHandler.RefreshStockData),
    path('Stream/Get', fyersStreamDataHandler.GetData),
    #Strategies
    path('Strategy/Straddle', fyersStrategiesHandler.StraddleOrder),
    path('Strategy/Active', fyersStrategiesHandler.GetActiveStrategies),
]
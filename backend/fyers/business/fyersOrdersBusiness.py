from .fyersSessionBusiness import FyersSessionBusiness
from ..fyersConstants import BuyorSellSide, OrderType, ProductType, Validity

fyersSession = FyersSessionBusiness()

class FyersOrderManagementBusiness():

    def __init__(self) -> None:
        pass

    def GetOrderBook(self):
        return fyersSession.fyers_session_model.orderbook()
    
    def GetOrderStatus(self, orderId):
        reqdata = {"id": orderId}
        return fyersSession.fyers_session_model.orderbook(data=reqdata)

    def GetPositions(self):
        return fyersSession.fyers_session_model.positions()

    def GetTradeBook(self):
        return fyersSession.fyers_session_model.tradebook()

    def LimitOrder(self, symbol, qty, price, buyorsell):
        ordertype = BuyorSellSide.Buy.value if buyorsell == 'Buy' else (BuyorSellSide.Sell.value if buyorsell == 'Sell' else '')

        reqdata = {
                "symbol":f"{symbol}",
                "qty":{qty},
                "type":{OrderType.Limit_Order.value},
                "side":{ordertype},
                "productType":f"{ProductType.INTRADAY.name}",
                "limitPrice":price,
                "stopPrice":0,
                "validity":f"{Validity.DAY}",
                "disclosedQty":0,
                "offlineOrder":"False",
                "stopLoss":0,
                "takeProfit":0
        }
        res = fyersSession.fyers_session_model.place_order(data=reqdata)
        return res
    
    def MarketOrder(self, symbol, qty, buyorsell):
        ordertype = BuyorSellSide.Buy.value if buyorsell == 'Buy' else (BuyorSellSide.Sell.value if buyorsell == 'Sell' else '')
        
        reqdata = {
                "symbol":f"{symbol}",
                "qty":qty,
                "type":OrderType.Market_Order.value,
                "side":ordertype,
                "productType":f"{ProductType.INTRADAY.name}",
                "limitPrice":0,
                "stopPrice":0,
                "validity":f"{Validity.DAY.name}",
                "disclosedQty":0,
                "offlineOrder":"False",
                "stopLoss":0,
                "takeProfit":0
        }
        print(f'MarketOrder {reqdata}')
        return self.SingleOrder(data=reqdata)

    def SingleOrder(self, data):
        return fyersSession.fyers_session_model.place_order(data= data)

    def ModifyOrder(self, orderid, limitPrice, quantity):
        reqdata = {
            "id":orderid, 
            "type":1, 
            "limitPrice": limitPrice,
            "qty":quantity
        }
        return fyersSession.fyers_session_model.modify_order(data=reqdata)
    
    def CancelOrder(self, orderId):
        reqdata = {
            "id":orderId
        }
        return fyersSession.fyers_session_model.cancel_order(data=reqdata)

    def ExistPosition(self, orderId):
        reqdata = {
            "id":orderId
        }
        return fyersSession.fyers_session_model.exit_positions(data=reqdata)
    
    def MultipleOrders(self, data):
        return fyersSession.fyers_session_model.place_basket_orders(data=data)
        
    def CancelOrders(self, orderList):
        return fyersSession.fyers_session_model.cancel_basket_orders(data=orderList)
    
    def ExistMultiplePositions(self,orderList):
        return fyersSession.fyers_session_model.exit_positions(data=orderList)

    def MarketStatus(self):
        return fyersSession.fyers_session_model.market_status()
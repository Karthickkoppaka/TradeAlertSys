import enum
import json
from types import SimpleNamespace

class OrderType(enum.Enum):
    Limit_Order = 1 
    Market_Order = 2 
    Stop_Order_SLM = 3
    Stoplimit_Order_SLL = 4

class BuyorSellSide(enum.Enum):
    Buy = 1
    Sell = -1

class ProductType(enum.Enum):
    CNC = 1 #For equity only
    INTRADAY = 2 #Applicable for all segments.
    MARGIN = 3 #Applicable only for derivatives
    CO = 4 #Cover Order
    BO = 5 #Bracket Order

class Validity(enum.Enum):
    IOC = 1 #Immediate or Cancel
    DAY = 2 #Valid till the end of the day

class InstrumentTypes(enum.Enum):
    FUTIDX = 11
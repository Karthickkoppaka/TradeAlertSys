from django.test import TestCase

# Create your tests here.
import pandas as pd
data =  [{"index": 0, "Id": 355275, "Strategy": "Straddle", "TargetSymbol": "NSE:SBIN-EQ", "EnquieTimeStamp": 1662321624668, "TriggerPrice": 15000, "CurrentPrice": 536.7, "QueueStatus": "Pending", "TargetOptionCE": "NSE:SBIN-EQ", "TargetOptionPE": "NSE:SBIN-EQ"}]
colEnq = ['Id', 'Strategy', 'TargetSymbol', 'EnquieTimeStamp', 'TriggerPrice', 'CurrentPrice','QueueStatus', 'TargetOptionCE', 'TargetOptionPE' ]
fyersStategiesEnque = pd.DataFrame(data, columns=colEnq)
id = 355275
fyersStategiesEnque = fyersStategiesEnque[fyersStategiesEnque['Id'] != id]
print(fyersStategiesEnque)

#dfm = df[df['Id'] != id]
#print(dfm)
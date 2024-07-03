from datetime import date, timedelta
import pandas as pd
from binance import Client
today = date.today()
yesterday = today - timedelta(days=1)
def criptodata(dataticker):
    api_key = "pPHHzDYZipYmbSTK2PzNxl11htjcVBHKjdpcE1Qj4IJqFbXH37HTNbB8FhpQpCEI"
    api_secret = "qy23N3I9hXYHYNmaRboj43z0c3Huupqce3eermzPHff8vGaw8GLrWTOSGgmaIRHx"
    #https://testnet.binance.vision/
    client = Client(api_key, api_secret)
    price = client.get_symbol_ticker(symbol=dataticker)
    print(price)
    asset = dataticker
    start = "2017.8.17"
    end = str(yesterday)
    timeframe = "1h"
    df = pd.DataFrame(client.get_historical_klines(asset,timeframe,start,end))
    df = df.iloc[:,:6]
    df.columns = ["Date","Open","High","Low","Close","Volume"]
    df = df.set_index("Date")
    df.index = pd.to_datetime(df.index, unit="ms")
    df = df.astype("float")
    print(df)
    #grabar en csv:
    df.to_csv(dataticker + "3.csv", encoding='utf-8')
    print("Data extraction finished :)")
list = ["BTCUSDT"]
for i in list:
    criptodata(i)

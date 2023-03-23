import requests
import app

# In the code below we first set the api to the SetApi function in app.py. We then use the information returned from the UI to
# get the symbol of the stock data the user is wishing to view, before running it through the url variable with retrieves
# the data from the API.

# To access one of these variables you will first need to use the following example,
#import app
#stock_data = app.GetStock()
#symbol = stock_data["symbol"]

def pullStock():
    url = f"https://www.alphavantage.co/query?function={app.GetTimeSeries()}&symbol={app.GetStockSymbol()}&apikey={app.GetApi()}"
    r = requests.get(url)
    data = r.json()
    stock_data = data["Global Quote"]

    app.SetStock({
    "symbol": stock_data["01. symbol"],
    "open": stock_data["02. open"],
    "high": stock_data["03. high"],
    "low": stock_data["04. low"],
    "price": stock_data["05. price"],
    "volume": stock_data["06. volume"],
    "last_refreshed": stock_data["07. latest trading day"],
    "previous_close": stock_data["08. previous close"],
    "change": stock_data["09. change"],
    "change_percent": stock_data["10. change percent"]
})



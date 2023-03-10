
# This document will contain functions to generate a graph from data and then display it in the browser
import requests, pygal, lxml
from datetime import datetime

# Example API request for testing
json = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo").json()
data = [{"date": k, **v} for k, v in json["Time Series (5min)"].items()]

print(data[0])



date_string = '2023-03-09 11:05:00'



#   Data as a JSON Obj
def create_line_graph(data):
    line = pygal.DateTimeLine(
        x_label_rotation=35, truncate_label=-1,
        x_value_formatter=lambda dt: dt.strftime('%d, %b %Y at %I:%M:%S %p')
    )

    data["Time Series (5min)"]
    
    open = []
    high = []
    low = []
    close = []
    volumne = []


    for item in data:
        line.add("")

    line.add("Serie", [
        (datetime(2013, 1, 2, 12, 0), 300),
        (datetime(2013, 1, 12, 14, 30, 45), 412),
        (datetime(2013, 2, 2, 6), 823),
        (datetime(2013, 2, 22, 9, 45), 672)
    ])



def string_to_datetime(date):
    date_format = '%Y-%m-%d %H:%M:%S'
    return datetime.strptime(date, date_format)







# This document will contain functions to generate a graph from data and then display it in the browser
import requests, pygal, lxml
from datetime import datetime

# Example API request for testing
json = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo").json()
data = [{"date": k, **v} for k, v in json["Time Series (5min)"].items()]

print(data[0])


options_template = {
    "Open": [],
    "High": [],
    "Low": [],
    "Close": [],
    "Volume": []
}

#   Data as a JSON Obj
def append_data(data, graph):
    options = options_template.copy()
    for item in data:
        date = string_to_datetime(item["date"])
        options["Open"].append((date, float(item["1. open"])))
        options["High"].append((date, float(item["2. high"])))
        options["Low"].append((date, float(item["3. low"])))
        options["Close"].append((date, float(item["4. close"])))
        options["Volume"].append((date, float(item["5. volume"])))

    print(options["Volume"])

    for opt in options:
        graph.add(opt, options[opt])
    return graph

#   Converts date string to datetime object
def string_to_datetime(date):
    date_format = '%Y-%m-%d %H:%M:%S'
    return datetime.strptime(date, date_format)

def get_date(item):
    return item["date"]

def create_line_graph(data):
    line = pygal.DateTimeLine(
        x_label_rotation=35, truncate_label=-1,
        x_value_formatter=lambda dt: dt.strftime('%d, %b %Y at %I:%M:%S %p')
    )
    line = append_data(data, line)
    line.render_in_browser()

def create_bar_graph(data):

    data.sort(key = get_date)

    line = pygal.Bar()
    line = append_data(data, line)
    line.render_in_browser()

# create_bar_graph(data)
create_line_graph(data)
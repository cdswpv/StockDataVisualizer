
# This document will contain functions to generate a graph from data and then display it in the browser
import requests, pygal, lxml
from datetime import datetime

# Example API request for testing
json = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo").json()
data = [{"date": k, **v} for k, v in json["Time Series (5min)"].items()]


options_template = {
    "Open": [],
    "High": [],
    "Low": [],
    "Close": []
}

def create_line_graph(data: dict):
    '''
    Creates a Line Graph of given data and displays in the user's default browser.

    Parameters:
        data: A dictionary representation of the data JSON.
    '''
    create_graph(data, pygal.Line())

def create_bar_graph(data):
    '''
    Creates a Bar Graph of given data and displays in the user's default browser.

    Parameters:
        data: A dictionary representation of the data JSON.
    '''
    create_graph(data, pygal.Bar())

#   Data as a JSON Obj/Dictionary
def create_graph(data, graph):
    '''
    Creates a graph from the given data and displays it in the user's default browser.

    Parameters:
        data: A dictionary representation of the data JSON.
        graph: A pygal graph object (pygal.Bar() & pygal.Line() are known to work)
    '''
    options = options_template.copy()
    dates = []
    data.sort(key = get_date)

    #   Format data from JSON to be used by graph
    for item in data:
        dates.append(string_to_datetime(item["date"]))
        options["Open"].append(float(item["1. open"]))
        options["High"].append(float(item["2. high"]))
        options["Low"].append(float(item["3. low"]))
        options["Close"].append(float(item["4. close"]))

    #   Add Data to graph
    for opt in options:
        graph.add(opt, options[opt])

    #   Graph Setup and Render
    graph.x_label_rotaion = 20
    graph.x_labels = dates
    graph.render_in_browser()

#   Converts date string to datetime object
def string_to_datetime(date: str):
    '''
    Converts a string date in format YYYY-MM-DD HH:MM:SS to a datetime object

    Parameters:
        date: String date in format YYYY-MM-DD HH:MM:SS

    Returns:
        datetime object
    '''
    date_format = '%Y-%m-%d %H:%M:%S'
    return datetime.strptime(date, date_format)

#   Used to sort the data array by each dict's  "date" key
def get_date(item: dict):
    '''
    Gets the value of "date" from a dictionary
    '''
    return item["date"]

#   Test calls
# create_bar_graph(data)
create_line_graph(data)
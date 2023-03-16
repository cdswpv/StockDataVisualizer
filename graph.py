
# This document will contain functions to generate a graph from data and then display it in the browser
import requests, pygal, lxml, re
from datetime import datetime

# Example API request for testing

query1 = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=15min&apikey=demo"
query2 = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo"
query3 = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=15min&apikey=ELUE44GZIWWXQ78B"

json = requests.get(query3).json()
# data = [{"date": k, **v} for k, v in json["Time Series (5min)"].items()]

# symbol = json["Meta Data"]["2. Symbol"]

# regex = re.compile("Time Series .*")

# time_series = json[[key for key in json.keys() if re.match(r"Time Series .*", key)][0]]
# data = [{"date": k, **v} for k, v in (
#     json[
#         [key for key in json.keys() if re.match(r"Time Series .*", key)][0]
# ])]


# if "Time Series (5min)" in data:
#     key = "Time Series (5min)"
# elif "Time Series (Daily)" in data:
#     key = "Time Series (Daily)"
# elif "Time Series (Weekly)" in data:
#     key = "Time Series (Weekly)"



options_template = {
    "Open": [],
    "High": [],
    "Low": [],
    "Close": []
}

def create_line_graph(json: dict):
    '''
    Creates a Line Graph of given data and displays in the user's default browser.

    Parameters:
        json: A dictionary representation of the data JSON.
    '''
    create_graph(json, pygal.Line())

def create_bar_graph(json: dict):
    '''
    Creates a Bar Graph of given data and displays in the user's default browser.

    Parameters:
        json: A dictionary representation of the data JSON.
    '''
    create_graph(json, pygal.Bar(x_label_rotation=90))

#   Data as a JSON Obj/Dictionary
def create_graph(json: dict, graph):
    '''
    Creates a graph from the given data and displays it in the user's default browser.

    Parameters:
        json: A dictionary representation of the data JSON.
        graph: A pygal graph object (pygal.Bar() & pygal.Line() are known to work)
    '''
    dates = []
    options = options_template.copy()
    #   Extracts the data points from the JSON, now reformatted and sorted
    data = extract_data(json)
    # title = create_title(symbol, data);

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
    # graph.x_label_rotaion = 90
    graph.x_labels = dates
    # graph.width = 5000
    # graph.height=2000
    graph.render_in_browser()

#   Converts date string to datetime object
def string_to_datetime(date: str):
    '''
    Converts a string date in format YYYY-MM-DD HH:MM:SS to a datetime object

    Parameters:
        date: String date in format YYYY-MM-DD w/ optional time formatting HH:MM:SS

    Returns:
        datetime object
    '''
    if re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", date) is not None:  #   Format YYYY-MM-DD HH:MM:SS
        date_format = '%Y-%m-%d %H:%M:%S'
    elif re.match(r"\d{4}-\d{2}-\d{2}", date) is not None:                  #   Format YYYY-MM-DD
        date_format = '%Y-%m-%d'
    return datetime.strptime(date, date_format)

#   Used to sort the data array by each dict's  "date" key
def get_date(item: dict):
    '''
    Gets the value of "date" from a dictionary
    '''
    return item["date"]

def extract_data(json: dict):
    # return [{"date": k, **v} for k, v in json[[key for key in json.keys() if re.match(r"Time Series .*", key)][0]].items()].sort(key = get_date) # this is an incredibly unreadable piece of code.

    #   Finds the "Time Series" key within the dictionary, whether it is "Time Series (Daily)", "... (Monthly)", or "... (15min)"
    #   Loops through keys, checks if they match, then will return the first (and only) instance
    time_series = [k for k in json.keys() if re.match(r"Time Series .*", k)][0]
    #   Takes each line that looks like this: "YYYY-MM-DD": {"key1": "value1", "key2": "value2"}
    #   Converts it to this {"date": "YYYY-MM-DD", "key1": "value1", "key2": "value2"}
    #   And places them all into a list
    data_points = [{"date": k, **v} for k, v in json[time_series].items()]
    #   Sorts the list using the get_date function and returns it
    data_points.sort(key = get_date)
    return data_points

    # data = [{"date": k, **v} for k, v in json["Time Series (5min)"].items()]

# def create_title(symbol: str, data: list[dict[str, any]]):
#     day_optional = ""
#     start = data[0]["date"]
#     end = data[len(data)]["date"]

#     return f"Stock Data for {symbol}: {day_optional} {start} to {end}"

#   Test calls
create_bar_graph(json)
# create_line_graph(json)

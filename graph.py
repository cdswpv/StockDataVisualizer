import requests, pygal, lxml, re, app
from datetime import datetime
from pygal.style import Style

#####  Example API request for testing, will NOT be in final  #####

query1 = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=15min&apikey=demo"
query2 = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo"
query3 = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=15min&apikey=ELUE44GZIWWXQ78B"

json = requests.get(query3).json()

#####  Functions accessable from outside  #####
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
    create_graph(json, pygal.Bar())

#####  Functions not to be accessed  #####
def create_graph(json: dict, graph):
    '''
    Creates a graph from the given data and displays it in the user's default browser.

    Parameters:
        json: A dictionary representation of the data JSON.
        graph: A pygal graph object (pygal.Bar() & pygal.Line() are known to work)
    '''
    dates = []
    options = { "Open": [], "High": [], "Low": [], "Close": [] }

    #   Extracts the data points from the JSON, now reformatted and sorted
    data = extract_data(json)

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
    graph.style = Style(
        label_font_size = 30,
        stroke_width = 15,
        legend_font_size = 50,
        title_font_size = 70
    )
    graph.dots_size = 15
    graph.x_labels = dates
    graph.x_label_rotation = 90
    graph.width =(len(dates) * 50)
    graph.height = len(dates) * 25
    graph.title = create_title()

    graph.render_in_browser()

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

def get_date(item: dict):
    '''
    Gets the value of "date" from a dictionary (used for sorting)
    '''
    return item["date"]

def extract_data(json: dict):
    '''
    Reformats the JSON response into an array containing each data point as a self contained dictionary.

    Parameters:
        json: A dictionary representing the response from the API

    Returns:
        Array of the newly minted data points. list[dict[str, Any]]
    '''
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




def create_title():
    '''
    Creates the title for the graph using data from app.py.
    
    Returns:
        Title as string.
    '''
    symbol = app.GetStockSymbol()
    begin = app.GetBeginningDate()
    end = app.GetEndDate()
    return f"Data for {symbol} From {begin} to {end}"


#####  Test calls  #####
# create_bar_graph(json)
create_line_graph(json)

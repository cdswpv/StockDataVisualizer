import ui
import graph
import api
import error

api = "ARJ4YHDD7BSSD94B"
stockSymbol = None
stock = None
chartType = None
timeSeries = None
bDate = None
eDate = None

#Main function needs to accept input and send output to the ui.py file.
def Main():
    #Call function in ui.py that begins the interaction between the user and system
    print("Stock Data Visualizer\n--------------------")
    #SetStockSymbol(ui.get_stock_symbol())
    SetChartType(ui.get_chart_type())
    SetTimeSeries(ui.get_time_series())
    SetDates(ui.get_dates())

    if not ui.restart_program():
            #break
            return
    return

########################
#This is the Set Section
#These are things/functions for me to grab information
########################

def SetStockSymbol(x):
    #Gets input from UI and sets the stock symbol
    global stockSymbol
    stockSymbol = x

def SetStock(new_stock_data):
    global stock
    stock = new_stock_data

def SetChartType(x):
    #Gets input from UI to determine the chart that they would like to use
    global chartType
    chartType = x

def SetTimeSeries(x):
    #Gets input from UI and chooses a time series
    #Intraday, Daily, Weekly, Monthly
    global timeSeries
    timeSeries = x

def SetDates(x, y):
    #Gets input from UI to set the beginning date for the charts
    #Must be a correct formart (error check)
    global bDate
    bDate = x
    global eDate
    eDate = y     

########################
#This is the Get Section
########################
#To use these functions from other files (dont type the quotation marks):
#You must have "import app" in the beginning of you file, like mine does
#Then when calling the function you just type it with "app.functionname(parameter)"
########################
def GetApi():
    #Returns the api key
    return api

def GetStockSymbol():
    #Returns the stock symbol
    return stockSymbol

def GetStock():
    return stock
    
def GetChartType():
    #Returns the chart type
    return chartType

def GetTimeSeries():
    #Returns the chosen time series
    #Intraday, Daily, Weekly, Monthly
    return timeSeries

def GetBeginningDate():
    #Returns the beginning date
    #Must be a correct formart (error check)
    return bDate

def GetEndDate():
    #returns the end date
    #Must be a correct formart (error check)
    #Cannot be before the beginning date (error check)
    return eDate

Main()
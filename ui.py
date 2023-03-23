from datetime import datetime
import app
import graph
def get_stock_symbol():
    stockSymbol = input("Enter the stock Symbol you are looking for: ")
    print(stockSymbol)
    return stockSymbol

def get_chart_type():
    valid_chart_type = False
    while not valid_chart_type:
        chartType = input("Chart Types\n----------\n1. Bar\n2. Line\nEnter the chart type you want (1, 2): ")
        if chartType == '1':
            print("Bar")
            graph.create_bar_graph()
            valid_chart_type = True
        elif chartType == '2':
            print("Line")
            graph.create_line_graph()
            valid_chart_type = True
        else:
            print("Invalid input. Please enter 1 or 2.")
    return chartType

def get_time_series():
    valid_time_type = False
    while not valid_time_type:
        timeSeries = input("Select the time series of the chart you want to generate\n--------------------------\n1. Intradaily\n2. Daily\n3. Weekly\n4. Monthly\nEnter the time series option (1, 2, 3, 4): ")
        if timeSeries == '1':
            print("Intraday")
            return "TIME_SERIES_INTRADAY"
            valid_time_type = True
        elif timeSeries == '2':
            print("Daily")
            return "TIME_SERIES_DAILY"
            valid_time_type = True
        elif timeSeries == '3':
            print("Weekly")
            return "TIME_SERIES_WEEKLY"
            valid_time_type = True
        elif timeSeries == '4':
            print("Monthly")
            return "TIME_SERIES_MONTHLY"
            valid_time_type = True
        else:
            print("Invalid input. Please enter 1, 2, 3 or 4.")

def get_dates():
    while True:
        try:
            bDate = input("Enter the start date in format (YYYY-MM-DD): ")
            bDate = datetime.strptime(bDate, "%Y-%m-%d")
            bDate_str = bDate.strftime("%Y-%m-%d")
            print(bDate.strftime("%Y-%m-%d"))
            eDate = input("Enter the ending date in format (YYYY-MM-DD): ")
            eDate = datetime.strptime(eDate, "%Y-%m-%d")
            eDate_str = eDate.strftime("%Y-%m-%d")
            print(eDate.strftime("%Y-%m-%d"))
            if bDate > eDate:
                print("Error: Start date must be before end date.")
            else:
                return(bDate_str, eDate_str)
        except ValueError:
            print("Error: Invalid date format. Please enter a date in the format YYYY-MM-DD.")
            #if the user enteres a end date before the start date it will ask for the start date again.
def restart_program():
    restart = input("Do you want to restart the program? (y/n): ")
    return restart.lower() == 'y'
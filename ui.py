from datetime import datetime
import app
def get_stock_symbol():
    stockSymbol = input("Enter the stock Symbol you are looking for: ")
    print(stockSymbol)
    app.SetStockSymbol(get_stock_symbol())

def get_chart_type():
    valid_chart_type = False
    while not valid_chart_type:
        chartType = input("Chart Types\n----------\n1. Bar\n2. Line\nEnter the chart type you want (1, 2): ")
        if chartType == '1':
            print("Bar")
            valid_chart_type = True
        elif chartType == '2':
            print("Line")
            valid_chart_type = True
        else:
            print("Invalid input. Please enter 1 or 2.")
    app.SetChartType(get_chart_type())

def get_time_series():
    valid_time_type = False
    while not valid_time_type:
        timeSeries = input("Select the time series of the chart you want to generate\n--------------------------\n1. Intradaily\n2. Daily\n3. Weekly\n4. Monthly\nEnter the time series option (1, 2, 3, 4): ")
        if timeSeries == '1':
            print("Intradaily")
            valid_time_type = True
        elif timeSeries == '2':
            print("Daily")
            valid_time_type = True
        elif timeSeries == '3':
            print("Daily")
            valid_time_type = True
        elif timeSeries == '4':
            print("Weekly")
            valid_time_type = True
        else:
            print("Invalid input. Please enter 1, 2, 3 or 4.")
        app.SetTimeSeries(get_time_series())

def get_dates():
    while True:
        try:
            bDate = input("Enter the start date in format (YYYY-MM-DD): ")
            bDate = datetime.strptime(bDate, "%Y-%m-%d")
            print(bDate.strftime("%Y-%m-%d"))
            eDate = input("Enter the ending date in format (YYYY-MM-DD): ")
            eDate = datetime.strptime(eDate, "%Y-%m-%d")
            print(eDate.strftime("%Y-%m-%d"))
            if bDate > eDate:
                print("Error: Start date must be before end date.")
            else:
                app.SetBeginningDate(bDate())
                app.SetEndDate(eDate())
        except ValueError:
            print("Error: Invalid date format. Please enter a date in the format YYYY-MM-DD.")
            #if the user enteres a end date before the start date it will ask for the start date again.
def restart_program():
    restart = input("Do you want to restart the program? (y/n): ")
    return restart.lower() == 'y'

def main():
    while True:
        print("Stock Data Visualizer\n--------------------")
        stockSymbol = get_stock_symbol()
        chartType = get_chart_type()
        timeSeries = get_time_series()
        bDate, eDate = get_dates()

        if not restart_program():
            break

main()

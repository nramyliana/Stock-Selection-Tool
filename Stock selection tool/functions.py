
import csv #to read and write csv file
import pandas as pd #to make the data more structured
import yfinance as yf #to fetch historical closing price
import os #to check the csv file exist or not

""" Register a new user and store their credentials securely."""
def register_user(email,password):
    users = []

    if os.path.exists('users.csv'):
        with open('users.csv', mode='r') as file:    #if the file exist, then it will read the file
            reader = csv.reader(file)
            for row in reader:
                users.append(row)
                if row[0] ==email:
                    print("Email has been registered! :)")   #if the email entered in the file then, it will inform the users that the email has been registered
                    return False
    else:
        print("User file doesn't exist. The file is being created now.")  #this is when the os identify the file is not exist yet, so the file will be created

    users.append([email,password])
    with open('users.csv', mode='w',newline = '') as file:
        writer=csv.writer(file)
        writer.writerows(users)                                     #this is when the email is not registered yet, so the csv will write the email and password in users.scv                                                       

    print("Your registration is successful! :)")
    return True

"""Verify user login credentials."""
def authenticate_user(email,password):
    if os.path.exists('users.csv'):
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] ==email and row[1]==password:
                    return True
    return False

"""Fetch historical closing prices for the given stock ticker and period using YFinance."""
def get_closing_prices(ticker,start_date,end_date):
    stock_data=yf.download(ticker,start=start_date,end=end_date)
    if 'Close' in stock_data.columns:
        return stock_data['Close']
    else:
        print("No closing price available.")
        return None

"""Perform basic analysis on the closing prices:
-Average closing price.
-Percentage change.
-Highest and lowest closing prices."""

def analyze_closing_prices(data):
    if data.empty:
        print("No closing price available. ")
        return None
    average=data.mean().item()
    percentage_change=((data.iloc[-1]-data.iloc[0])/data.iloc[0]*100).item()
    highest=data.max().item()
    lowest = data.min().item()

    return(average,percentage_change,highest,lowest)


"""Save user interactions (email, stock ticker, analysis results) to a CSV file."""
def save_to_csv(data,filename):
    df=pd.DataFrame(data)
    header=not os.path. exists(filename)
    df.to_csv(filename,mode='a',index=False, header=header)
    print("Data has been succesfully saved! :) ")

"""Retrieve and display saved data from the CSV file."""
def read_from_csv(filename):
    if os.path.exists(filename):                #when the user want to retrieve the saved data, it will read and display the data to user
        data=pd.read_csv(filename)
        print(data)
    else:
        print("No data found")
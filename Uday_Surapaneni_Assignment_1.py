#Q1
import random
import pandas as pd
import numpy as np
import math

# Task 1: Create a dictionary to represent the stock portfolio
stock_portfolio = {}

# Task 2: Implement a function buy_stock()
def buy_stock(stock_symbol, num_shares, purchase_price):
    if stock_symbol in stock_portfolio:
        stock_portfolio[stock_symbol]['num_shares'] += num_shares
        stock_portfolio[stock_symbol]['purchase_price'] = purchase_price
    else:
        stock_portfolio[stock_symbol] = {
            'num_shares': num_shares,
            'purchase_price': purchase_price
        }

# Task 3: Implement a function sell_stock()
def sell_stock(stock_symbol, num_shares_to_sell):
    if stock_symbol in stock_portfolio:
        if stock_portfolio[stock_symbol]['num_shares'] >= num_shares_to_sell:
            stock_portfolio[stock_symbol]['num_shares'] -= num_shares_to_sell
        else:
            print("Not enough shares to sell.")
    else:
        print("Stock symbol not found in the portfolio.")

# Task 4: Implement a function calculate_portfolio_value()
def calculate_portfolio_value():
    total_value = 0
    for stock_symbol, stock_info in stock_portfolio.items():
        purchase_price = stock_info['purchase_price']
        current_price = purchase_price + (purchase_price * random.uniform(-0.20, 0.20))
        total_value += current_price * stock_info['num_shares']
    return total_value

# Task 5: Implement a function portfolio_performance()
def portfolio_performance():
    initial_investment = sum(stock_info['num_shares'] * stock_info['purchase_price'] for stock_info in stock_portfolio.values())
    current_value = calculate_portfolio_value()
    percentage_change = ((current_value - initial_investment) / initial_investment) * 100
    return percentage_change

# Create a menu-driven program
def main():
    while True:
        print("\n--- Stock Portfolio Management Menu ---")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Calculate Portfolio Value")
        print("5. Check Portfolio Performance")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            stock_symbol = input("Enter the stock symbol: ")
            num_shares = int(input("Enter the number of shares to buy: "))
            purchase_price = float(input("Enter the purchase price per share: "))
            buy_stock(stock_symbol, num_shares, purchase_price)

        elif choice == '2':
            stock_symbol = input("Enter the stock symbol: ")
            num_shares_to_sell = int(input("Enter the number of shares to sell: "))
            sell_stock(stock_symbol, num_shares_to_sell)

        elif choice == '3':
            print("\n--- Current Portfolio ---")
            for stock_symbol, stock_info in stock_portfolio.items():
                print(f"{stock_symbol}: {stock_info['num_shares']} shares, Purchase Price: {stock_info['purchase_price']}")

        elif choice == '4':
            portfolio_value = calculate_portfolio_value()
            print(f"\nPortfolio Value: {portfolio_value:.2f}")

        elif choice == '5':
            performance = portfolio_performance()
            print(f"\nPortfolio Performance: {performance:.2f}%")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


#Q2
def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Test the function
start_range = 1
end_range = 50
expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
result = find_prime_numbers(start_range, end_range)

if result == expected_primes:
    print("Congratulations! The function is correct.")
else:
    print("Too bad! There's a bug in the function.")

#Q3

def generate_random_time_series_data(proportion_to_delete=0.2):
    #Create a date range for the year 2020, +20 business days
    date_range=pd.date_range(start='2020-01-01',end='2021-01-20',freq='B')
    
    # Generate random data for a business day
    random_data=np.random.rand(len(date_range))
    
    #Create a dataframe with the date and the random generated data
    timeseries_data=pd.DataFrame({'Date':date_range,'Value':random_data})
    
    #Randomly delete some observations based on the given proportion
    num_observations_to_delete=int(proportion_to_delete * len(timeseries_data))
    indices_to_delete=np.random.choice(timeseries_data.index,num_observations_to_delete,replace=False)
    timeseries_data.drop(indices_to_delete,inplace=True)
    
    return timeseries_data

time_series_data=generate_random_time_series_data(proportion_to_delete=0.2)
time_series_data.shape
time_series_data.isnull().sum()
time_series_data.head()
time_series_data.tail()


def calculate_tnn(observation_dates, t):
    tnn = None
    min_diff = float('inf')
    target_days = 10

    for i in range(1, len(observation_dates)):
        diff = (observation_dates[i] - observation_dates[t]).days
        if diff > 0:
            tnn_candidate = abs(target_days / diff - 1)
            if tnn_candidate <= min_diff:
                min_diff = tnn_candidate
                tnn = i
                
    return tnn

def calculate_return(observation_dates, t, tnn, risk_factor_values):
    Dt = observation_dates[t]
    Dtnn = observation_dates[tnn]
    rj_Dt = risk_factor_values[t]
    rj_Dtnn = risk_factor_values[tnn]

    time_diff = (Dtnn - Dt).days
    sqrt_days = math.sqrt(10 / time_diff)

    return math.log(rj_Dtnn/rj_Dt) * sqrt_days

def main():
    timeseries_data = generate_random_time_series_data()
    
    observation_dates = timeseries_data['Date'].tolist()
    risk_factor_values = timeseries_data['Value'].tolist()

    returns = []
    for t in range(len(observation_dates) - 1):
        tnn = calculate_tnn(observation_dates, t)
        return_10bd = calculate_return(observation_dates, t, tnn, risk_factor_values)
        returns.append(return_10bd)

    print("10-day business returns:")
    for i, return_10bd in enumerate(returns):
        print(f"Index {i}: {return_10bd}")

if __name__ == "__main__":
    main()


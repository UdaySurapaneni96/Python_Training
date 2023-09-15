{
 "cells": [
  {
   "cell_type": "raw",
   "id": "72b41305-65c8-4edf-8c41-fe43f393e0c8",
   "metadata": {
    "tags": []
   },
   "source": [
    "Stock Portfolio Management\n",
    "You have been tasked with developing a stock portfolio management system. The system should allow users to add stocks to their portfolio, buy and sell stocks, calculate the portfolio's value, and perform other related operations.\n",
    "\n",
    "Tasks:\n",
    "1.Create a dictionary to represent the stock portfolio. The keys should be the stock symbols (e.g., 'AAPL', 'GOOG'), and the values should be dictionaries containing information about each stock, such as the number of shares and the purchase price.\n",
    "\n",
    "2.Implement a function buy_stock() that allows users to buy stocks. The function should take the stock symbol, number of shares, and purchase price as input and add the stock to the portfolio.\n",
    "\n",
    "3.Implement a function sell_stock() that allows users to sell stocks. The function should take the stock symbol and the number of shares to sell as input and update the portfolio accordingly.\n",
    "\n",
    "4.Implement a function calculate_portfolio_value() that calculates the current value of the entire stock portfolio based on the current stock prices. Assume current price for any stock is current price = purchase price + [*random number between -20 and 20] % of purchase price.    \n",
    "*  e.g., 4.11%, 0%, -7.0%,20.0%, -13.5%, -20.0% etc\n",
    "\n",
    "5.Implement a function portfolio_performance() that calculates the overall performance of the portfolio. The performance can be measured as the percentage change in the portfolio value from the initial investment value.\n",
    "\n",
    "6.[Optional] Create a menu-driven program to allow users to interact with the stock portfolio management system. The program should provide options to buy, sell, view portfolio, calculate portfolio value, and check portfolio performance.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "73bcde37-1715-4243-9e33-db498971dde0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  1\n",
      "Enter the stock symbol:  TCS\n",
      "Enter the number of shares to buy:  10\n",
      "Enter the purchase price per share:  3355.40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  1\n",
      "Enter the stock symbol:  GAIL\n",
      "Enter the number of shares to buy:  100\n",
      "Enter the purchase price per share:  117.50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  1\n",
      "Enter the stock symbol:  MOTHERSON\n",
      "Enter the number of shares to buy:  100\n",
      "Enter the purchase price per share:  97.50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  1\n",
      "Enter the stock symbol:  BHARATIARTL\n",
      "Enter the number of shares to buy:  100\n",
      "Enter the purchase price per share:  895.10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Current Portfolio ---\n",
      "TCS: 10 shares, Purchase Price: 3355.4\n",
      "GAIL: 100 shares, Purchase Price: 117.5\n",
      "MOTHERSON: 100 shares, Purchase Price: 97.5\n",
      "BHARATIARTL: 100 shares, Purchase Price: 895.1\n",
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  2\n",
      "Enter the stock symbol:  TCS\n",
      "Enter the number of shares to sell:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Current Portfolio ---\n",
      "TCS: 8 shares, Purchase Price: 3355.4\n",
      "GAIL: 100 shares, Purchase Price: 117.5\n",
      "MOTHERSON: 100 shares, Purchase Price: 97.5\n",
      "BHARATIARTL: 100 shares, Purchase Price: 895.1\n",
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Portfolio Value: 152221.33\n",
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Portfolio Performance: -0.59%\n",
      "\n",
      "--- Stock Portfolio Management Menu ---\n",
      "1. Buy Stock\n",
      "2. Sell Stock\n",
      "3. View Portfolio\n",
      "4. Calculate Portfolio Value\n",
      "5. Check Portfolio Performance\n",
      "6. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-6):  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the program.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# Task 1: Create a dictionary to represent the stock portfolio\n",
    "stock_portfolio = {}\n",
    "\n",
    "# Task 2: Implement a function buy_stock()\n",
    "def buy_stock(stock_symbol, num_shares, purchase_price):\n",
    "    if stock_symbol in stock_portfolio:\n",
    "        stock_portfolio[stock_symbol]['num_shares'] += num_shares\n",
    "        stock_portfolio[stock_symbol]['purchase_price'] = purchase_price\n",
    "    else:\n",
    "        stock_portfolio[stock_symbol] = {\n",
    "            'num_shares': num_shares,\n",
    "            'purchase_price': purchase_price\n",
    "        }\n",
    "\n",
    "# Task 3: Implement a function sell_stock()\n",
    "def sell_stock(stock_symbol, num_shares_to_sell):\n",
    "    if stock_symbol in stock_portfolio:\n",
    "        if stock_portfolio[stock_symbol]['num_shares'] >= num_shares_to_sell:\n",
    "            stock_portfolio[stock_symbol]['num_shares'] -= num_shares_to_sell\n",
    "        else:\n",
    "            print(\"Not enough shares to sell.\")\n",
    "    else:\n",
    "        print(\"Stock symbol not found in the portfolio.\")\n",
    "\n",
    "# Task 4: Implement a function calculate_portfolio_value()\n",
    "def calculate_portfolio_value():\n",
    "    total_value = 0\n",
    "    for stock_symbol, stock_info in stock_portfolio.items():\n",
    "        purchase_price = stock_info['purchase_price']\n",
    "        current_price = purchase_price + (purchase_price * random.uniform(-0.20, 0.20))\n",
    "        total_value += current_price * stock_info['num_shares']\n",
    "    return total_value\n",
    "\n",
    "# Task 5: Implement a function portfolio_performance()\n",
    "def portfolio_performance():\n",
    "    initial_investment = sum(stock_info['num_shares'] * stock_info['purchase_price'] for stock_info in stock_portfolio.values())\n",
    "    current_value = calculate_portfolio_value()\n",
    "    percentage_change = ((current_value - initial_investment) / initial_investment) * 100\n",
    "    return percentage_change\n",
    "\n",
    "# Create a menu-driven program\n",
    "def main():\n",
    "    while True:\n",
    "        print(\"\\n--- Stock Portfolio Management Menu ---\")\n",
    "        print(\"1. Buy Stock\")\n",
    "        print(\"2. Sell Stock\")\n",
    "        print(\"3. View Portfolio\")\n",
    "        print(\"4. Calculate Portfolio Value\")\n",
    "        print(\"5. Check Portfolio Performance\")\n",
    "        print(\"6. Exit\")\n",
    "\n",
    "        choice = input(\"Enter your choice (1-6): \")\n",
    "\n",
    "        if choice == '1':\n",
    "            stock_symbol = input(\"Enter the stock symbol: \")\n",
    "            num_shares = int(input(\"Enter the number of shares to buy: \"))\n",
    "            purchase_price = float(input(\"Enter the purchase price per share: \"))\n",
    "            buy_stock(stock_symbol, num_shares, purchase_price)\n",
    "\n",
    "        elif choice == '2':\n",
    "            stock_symbol = input(\"Enter the stock symbol: \")\n",
    "            num_shares_to_sell = int(input(\"Enter the number of shares to sell: \"))\n",
    "            sell_stock(stock_symbol, num_shares_to_sell)\n",
    "\n",
    "        elif choice == '3':\n",
    "            print(\"\\n--- Current Portfolio ---\")\n",
    "            for stock_symbol, stock_info in stock_portfolio.items():\n",
    "                print(f\"{stock_symbol}: {stock_info['num_shares']} shares, Purchase Price: {stock_info['purchase_price']}\")\n",
    "\n",
    "        elif choice == '4':\n",
    "            portfolio_value = calculate_portfolio_value()\n",
    "            print(f\"\\nPortfolio Value: {portfolio_value:.2f}\")\n",
    "\n",
    "        elif choice == '5':\n",
    "            performance = portfolio_performance()\n",
    "            print(f\"\\nPortfolio Performance: {performance:.2f}%\")\n",
    "\n",
    "        elif choice == '6':\n",
    "            print(\"Exiting the program.\")\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "347203a3-3277-4f7b-8dd0-f18a5458da81",
   "metadata": {},
   "source": [
    "The above code is an implementation of a menu-driven program for managing a stock portfolio. Here's an explanation of the different parts of the code:\n",
    "\n",
    "1. Stock Portfolio Dictionary: The `stock_portfolio` dictionary is used to store information about the stocks in the portfolio. Each stock symbol is a key in the dictionary, and the corresponding value is another dictionary containing the number of shares and the purchase price.\n",
    "\n",
    "2. `buy_stock()` Function: This function is used to add or update a stock in the portfolio. It takes three parameters: `stock_symbol` (the symbol of the stock to buy), `num_shares` (the number of shares to buy), and `purchase_price` (the purchase price per share). If the stock symbol already exists in the portfolio, the function updates the number of shares and the purchase price. If the stock symbol is new, it adds a new entry to the portfolio.\n",
    "\n",
    "3. `sell_stock()` Function: This function is used to sell a specified number of shares of a stock from the portfolio. It takes two parameters: `stock_symbol` (the symbol of the stock to sell) and `num_shares_to_sell` (the number of shares to sell). If the stock symbol exists in the portfolio and the number of shares to sell is less than or equal to the number of shares in the portfolio, the function subtracts the sold shares from the portfolio.\n",
    "\n",
    "4. `portfolio_performance()` Function: This function calculates the percentage change in the portfolio value compared to the initial investment. It takes one parameter: `initial_investment` (the initial investment amount). It uses the `calculate_portfolio_value()` function (not shown in the code) to calculate the current value of the portfolio. It then calculates the percentage change and returns it.\n",
    "\n",
    "5. `main()` Function: This function is the main entry point of the program. It contains a while loop that displays a menu of options and prompts the user for their choice. Based on the user's choice, it calls the appropriate function to perform the desired action. The menu options include buying a stock, selling a stock, calculating portfolio performance, and exiting the program.\n",
    "\n",
    "6. Menu-Driven Program: The `main()` function uses a while loop to repeatedly display the menu and prompt the user for their choice. It then calls the corresponding function based on the user's choice. The loop continues until the user chooses to exit the program.\n",
    "\n",
    "The code is organized in a way that allows the user to interactively manage their stock portfolio by selecting options from the menu."
   ]
  },
  {
   "cell_type": "raw",
   "id": "938f249a-02bf-45e1-b82f-3b116a3d2f24",
   "metadata": {},
   "source": [
    "Q2)Debugging: Find Prime Numbers\n",
    "The goal of this function is to find all prime numbers in a given range (start to end).\n",
    "However, there are several bugs in the code that need to be fixed.\n",
    "Task. Debug given code and make sure it prints correct expected outcome. Explain in two lines, what are the changes you made. \n",
    "\n",
    "def is_prime(number):\n",
    "    if number == 1:\n",
    "        return False\n",
    "    for i in range(1, number):\n",
    "        if number / i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def find_prime_numbers(start, end):\n",
    "    prime_numbers = []\n",
    "    for num in range(start, end + 1):\n",
    "        if is_prime(num):\n",
    "            prime_numbers.append(num)\n",
    "    return prime_numbers\n",
    "\n",
    "# Test the function\n",
    "start_range = 1\n",
    "end_range = 50\n",
    "expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]\n",
    "result = find_prime_numbers(start_range, end_range)\n",
    "\n",
    "if result == expected_primes:\n",
    "print(\"Congratulations! The function is correct.\")\n",
    "else:\n",
    "    print(\"Too bad! There's a bug in the function.\")\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "4a734a21-5ac7-4001-9e38-a27242da42b4",
   "metadata": {},
   "source": [
    "Errors in the above code are as follows:\n",
    "1.In the is_prime function, we need to change the range to start from 2 instead of 1, as dividing by 1 will always result in the number being divisible.\n",
    "2.We need to change the division operator (/) to the modulus operator (%) to check for divisibility. If the remainder is 0, the number is not prime.\n",
    "\n",
    "The corrected code is as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dbecdf77-7041-4893-8dcf-d2a4a79f8aea",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Congratulations! The function is correct.\n"
     ]
    }
   ],
   "source": [
    "def is_prime(number):\n",
    "    if number == 1:\n",
    "        return False\n",
    "    for i in range(2, number):\n",
    "        if number % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def find_prime_numbers(start, end):\n",
    "    prime_numbers = []\n",
    "    for num in range(start, end + 1):\n",
    "        if is_prime(num):\n",
    "            prime_numbers.append(num)\n",
    "    return prime_numbers\n",
    "\n",
    "# Test the function\n",
    "start_range = 1\n",
    "end_range = 50\n",
    "expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]\n",
    "result = find_prime_numbers(start_range, end_range)\n",
    "\n",
    "if result == expected_primes:\n",
    "    print(\"Congratulations! The function is correct.\")\n",
    "else:\n",
    "    print(\"Too bad! There's a bug in the function.\")\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "a1c56be7-f93e-4216-bb60-48f39cc507c9",
   "metadata": {},
   "source": [
    "Obtaining the series of 10-business-days returns from the time series of observations as per given logic:\n",
    "Task 1. Generate input data using below func. (Saving you from all the hustle of reading a file. XD) \n",
    "Task 2. \n",
    "Obtain the series of 10-business-days returns for input data for period [2020-01-01,2020-12-31].\n",
    "1.Create one function to find the ‘nearest to 10 business days candidate’ \n",
    "2.And one main function to find the series of 10-business-days returns from the time series of observations and call ‘nearest to 10 business days candidate’ function within main function whenever needed. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "41d6e972-d314-4044-ad7b-8b160ecbb7bd",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "def generate_random_time_series_data(proportion_to_delete=0.2):\n",
    "    #Create a date range for the year 2020, +20 business days\n",
    "    date_range=pd.date_range(start='2020-01-01',end='2021-01-20',freq='B')\n",
    "    \n",
    "    # Generate random data for a business day\n",
    "    random_data=np.random.rand(len(date_range))\n",
    "    \n",
    "    #Create a dataframe with the date and the random generated data\n",
    "    timeseries_data=pd.DataFrame({'Date':date_range,'Value':random_data})\n",
    "    \n",
    "    #Randomly delete some observations based on the given proportion\n",
    "    num_observations_to_delete=int(proportion_to_delete * len(timeseries_data))\n",
    "    indices_to_delete=np.random.choice(timeseries_data.index,num_observations_to_delete,replace=False)\n",
    "    timeseries_data.drop(indices_to_delete,inplace=True)\n",
    "    \n",
    "    return timeseries_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3541fd62-36ad-409f-b6e0-b8ec1103108e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "time_series_data=generate_random_time_series_data(proportion_to_delete=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e80b9831-3d94-49c0-bda7-f173a43a8852",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(221, 2)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time_series_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0ac119ee-87f3-4375-aa20-ae21fab2ff8e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date     0\n",
       "Value    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time_series_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "da4f2160-e5a2-46d1-85c4-d34037c33bac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2020-01-01</td>\n",
       "      <td>0.851824</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2020-01-02</td>\n",
       "      <td>0.454168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-01-03</td>\n",
       "      <td>0.351585</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020-01-06</td>\n",
       "      <td>0.247110</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2020-01-07</td>\n",
       "      <td>0.551360</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Date     Value\n",
       "0 2020-01-01  0.851824\n",
       "1 2020-01-02  0.454168\n",
       "2 2020-01-03  0.351585\n",
       "3 2020-01-06  0.247110\n",
       "4 2020-01-07  0.551360"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time_series_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5c44b7ae-340a-486b-b818-f33839f15671",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>268</th>\n",
       "      <td>2021-01-11</td>\n",
       "      <td>0.754790</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>271</th>\n",
       "      <td>2021-01-14</td>\n",
       "      <td>0.615644</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>272</th>\n",
       "      <td>2021-01-15</td>\n",
       "      <td>0.114834</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>274</th>\n",
       "      <td>2021-01-19</td>\n",
       "      <td>0.551596</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>275</th>\n",
       "      <td>2021-01-20</td>\n",
       "      <td>0.887599</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Date     Value\n",
       "268 2021-01-11  0.754790\n",
       "271 2021-01-14  0.615644\n",
       "272 2021-01-15  0.114834\n",
       "274 2021-01-19  0.551596\n",
       "275 2021-01-20  0.887599"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time_series_data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a18fcd8b-4aa2-4e58-83b3-206c5b12cfd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10-day business returns:\n",
      "Index 0: -2.523970343491045\n",
      "Index 1: 0.48501969070006296\n",
      "Index 2: -0.6522262441640921\n",
      "Index 3: -0.26497468013933\n",
      "Index 4: 4.341867538387877\n",
      "Index 5: -0.1130211746150206\n",
      "Index 6: -0.5159342505196644\n",
      "Index 7: 2.2153355673928914\n",
      "Index 8: 0.6674542477722266\n",
      "Index 9: -1.195017636484704\n",
      "Index 10: -0.1963273147677913\n",
      "Index 11: 0.61080156484201\n",
      "Index 12: 0.4609184473894549\n",
      "Index 13: -0.16526977970824422\n",
      "Index 14: -0.34581933356813466\n",
      "Index 15: 1.0770561271746735\n",
      "Index 16: 0.11255138973357644\n",
      "Index 17: -1.5840444137257406\n",
      "Index 18: -1.8600517567370762\n",
      "Index 19: -1.8684824671654046\n",
      "Index 20: 0.013571098432732978\n",
      "Index 21: 3.854320911392516\n",
      "Index 22: -0.09574796439652981\n",
      "Index 23: 1.8426835799059598\n",
      "Index 24: 0.8642153805673235\n",
      "Index 25: 1.8584119198914633\n",
      "Index 26: -0.7727764320273932\n",
      "Index 27: -0.48123512110202826\n",
      "Index 28: -4.114922704994967\n",
      "Index 29: 0.36775352678425044\n",
      "Index 30: 0.2747589338116876\n",
      "Index 31: -1.3084673452281232\n",
      "Index 32: -1.219360556272223\n",
      "Index 33: 0.04977849057067416\n",
      "Index 34: 3.836873459506908\n",
      "Index 35: -0.22551216162016516\n",
      "Index 36: 1.522406686063904\n",
      "Index 37: 0.7956448467359202\n",
      "Index 38: -0.19470378185472909\n",
      "Index 39: -0.5235464044920813\n",
      "Index 40: 0.16785158703360908\n",
      "Index 41: -0.9939676667248779\n",
      "Index 42: -0.09069348825967777\n",
      "Index 43: -0.10159871031508579\n",
      "Index 44: -1.6478266632162877\n",
      "Index 45: 0.3600626580091072\n",
      "Index 46: -0.6458944112339082\n",
      "Index 47: 1.6655802198950924\n",
      "Index 48: -0.08641667600593246\n",
      "Index 49: 2.6255084840504557\n",
      "Index 50: 0.2008772902911305\n",
      "Index 51: 0.7372577048671021\n",
      "Index 52: 1.2879029010246426\n",
      "Index 53: 0.5953988727844108\n",
      "Index 54: 0.20243476917056447\n",
      "Index 55: 0.09892675664291488\n",
      "Index 56: 0.27514804245948804\n",
      "Index 57: -0.32048489885377585\n",
      "Index 58: -0.31495578375420613\n",
      "Index 59: -0.039694654597432474\n",
      "Index 60: -0.010448862660798341\n",
      "Index 61: -2.0390094964724303\n",
      "Index 62: -0.9484857689295795\n",
      "Index 63: -0.33124827028566317\n",
      "Index 64: -0.6114657671759683\n",
      "Index 65: -0.3701962194496082\n",
      "Index 66: -1.314636478912965\n",
      "Index 67: 0.15574773911251452\n",
      "Index 68: -0.565172424694451\n",
      "Index 69: -1.36610109922729\n",
      "Index 70: -1.9904183958415482\n",
      "Index 71: 0.40112708032553274\n",
      "Index 72: -0.012751033263061026\n",
      "Index 73: 0.09262642811054297\n",
      "Index 74: 2.228997703551565\n",
      "Index 75: 0.12627402321020822\n",
      "Index 76: -0.9388313879390986\n",
      "Index 77: 1.0993102560496957\n",
      "Index 78: 0.8565838681792637\n",
      "Index 79: -0.35370749300022386\n",
      "Index 80: -0.7802833879764984\n",
      "Index 81: 0.38661794608928096\n",
      "Index 82: -1.875332948506157\n",
      "Index 83: -1.4323186847278548\n",
      "Index 84: -0.053068908721495396\n",
      "Index 85: 0.6272292682635406\n",
      "Index 86: 0.11316873870195152\n",
      "Index 87: 2.1501121132173924\n",
      "Index 88: 0.41835123489487996\n",
      "Index 89: -0.04051361003813678\n",
      "Index 90: -3.621971888903016\n",
      "Index 91: -3.487449652106366\n",
      "Index 92: -0.7678192559163425\n",
      "Index 93: -1.5425930739583256\n",
      "Index 94: 0.5326925134156584\n",
      "Index 95: -1.947970416000985\n",
      "Index 96: -1.5577546313114385\n",
      "Index 97: 4.032730965079233\n",
      "Index 98: -0.48785405092892514\n",
      "Index 99: 1.5027262830778592\n",
      "Index 100: 1.9994421001813156\n",
      "Index 101: -0.32206806133961235\n",
      "Index 102: 0.38784912066112576\n",
      "Index 103: -0.03845174116388221\n",
      "Index 104: 0.46565448855153263\n",
      "Index 105: 0.06838420527118427\n",
      "Index 106: 0.94032160393111\n",
      "Index 107: 0.08668152342257499\n",
      "Index 108: 1.3422058197419935\n",
      "Index 109: -0.12495472410466664\n",
      "Index 110: -0.7303811376405839\n",
      "Index 111: 0.2816127721218972\n",
      "Index 112: -1.2172744957601203\n",
      "Index 113: -0.5806620917728993\n",
      "Index 114: -1.2553586176339457\n",
      "Index 115: 0.4800424076200341\n",
      "Index 116: -1.6410923297937348\n",
      "Index 117: -1.6482981437797348\n",
      "Index 118: -0.7638422248461888\n",
      "Index 119: -2.0430640412721215\n",
      "Index 120: 0.3053115439217178\n",
      "Index 121: 0.24825520934793577\n",
      "Index 122: 2.010440848125591\n",
      "Index 123: 0.713182197656389\n",
      "Index 124: 1.421941958085058\n",
      "Index 125: 0.6191020432859969\n",
      "Index 126: 3.2987398785978312\n",
      "Index 127: 0.6976351630889328\n",
      "Index 128: -0.24027924900521658\n",
      "Index 129: 2.1948808855823088\n",
      "Index 130: -0.47057976499349385\n",
      "Index 131: 1.3510877987252834\n",
      "Index 132: 0.015882692051791054\n",
      "Index 133: -0.3747940531860676\n",
      "Index 134: 0.44775928626112993\n",
      "Index 135: -1.339599078182915\n",
      "Index 136: 0.9079871434151431\n",
      "Index 137: 0.016045485021170813\n",
      "Index 138: -0.3823254662957683\n",
      "Index 139: -0.11592482139765313\n",
      "Index 140: -1.43587261147939\n",
      "Index 141: 0.5347612643091365\n",
      "Index 142: 0.37294360472747196\n",
      "Index 143: -0.09148991608904448\n",
      "Index 144: -1.367067465099423\n",
      "Index 145: -0.03421880573472162\n",
      "Index 146: -0.034513960252672206\n",
      "Index 147: 0.10492638864922611\n",
      "Index 148: -1.3046644756657517\n",
      "Index 149: 1.5495039312279308\n",
      "Index 150: -0.022426980140478524\n",
      "Index 151: 1.0309182266046513\n",
      "Index 152: 0.4600530221431337\n",
      "Index 153: -0.0014470877392904439\n",
      "Index 154: 0.976695443739596\n",
      "Index 155: -0.9584930421863825\n",
      "Index 156: -1.9350664214475368\n",
      "Index 157: -0.65620066277709\n",
      "Index 158: -2.1555727356620986\n",
      "Index 159: 0.30392866719234685\n",
      "Index 160: 0.9550041095231862\n",
      "Index 161: -0.18879420113193304\n",
      "Index 162: 0.9344536035838882\n",
      "Index 163: -1.223364552775413\n",
      "Index 164: -0.5192319862948391\n",
      "Index 165: 1.19626750995527\n",
      "Index 166: 2.08466316847939\n",
      "Index 167: 0.8902579088645748\n",
      "Index 168: -0.23043605217169594\n",
      "Index 169: 1.7145852686999317\n",
      "Index 170: 1.173341043187038\n",
      "Index 171: 0.5761425727242336\n",
      "Index 172: -0.5015212130675691\n",
      "Index 173: 0.08810224734436292\n",
      "Index 174: 0.13573692295975365\n",
      "Index 175: -1.541503153562224\n",
      "Index 176: -0.9510784843742388\n",
      "Index 177: 0.15536822862863506\n",
      "Index 178: 0.28683491089561947\n",
      "Index 179: 0.29942191459367956\n",
      "Index 180: -1.0303605371527544\n",
      "Index 181: 4.026589074196841\n",
      "Index 182: 1.1659311240291819\n",
      "Index 183: -0.22406645394937166\n",
      "Index 184: 0.04113596730706978\n",
      "Index 185: -0.2591214505658219\n",
      "Index 186: 0.762497274375338\n",
      "Index 187: 0.26605581689553737\n",
      "Index 188: 0.6929592964581689\n",
      "Index 189: 0.09228780868593146\n",
      "Index 190: -1.0727836208439365\n",
      "Index 191: 1.047538789401835\n",
      "Index 192: -0.9890512011287437\n",
      "Index 193: -1.3954947055588527\n",
      "Index 194: 0.1340685937979163\n",
      "Index 195: 1.8812736387629363\n",
      "Index 196: 0.12452066733009318\n",
      "Index 197: -0.8345723058572271\n",
      "Index 198: 1.161590884816717\n",
      "Index 199: 0.22003148885941068\n",
      "Index 200: -1.3012535329148454\n",
      "Index 201: 1.2866188878905205\n",
      "Index 202: -0.665050170076373\n",
      "Index 203: -0.7304406701492765\n",
      "Index 204: -0.2822581324387503\n",
      "Index 205: -0.5597707659892415\n",
      "Index 206: 1.5439501558058026\n",
      "Index 207: 0.6050625911978859\n",
      "Index 208: -0.01902572992591265\n",
      "Index 209: 0.6686076246597407\n",
      "Index 210: 0.016902330332612587\n",
      "Index 211: -0.4311286730425221\n",
      "Index 212: 1.1458388967192086\n",
      "Index 213: -2.00523758933255\n",
      "Index 214: -1.3181973329646135\n",
      "Index 215: -0.8560793049939194\n",
      "Index 216: -1.2481678524843918\n",
      "Index 217: -1.0757357444080926\n",
      "Index 218: 1.5505304060689862\n",
      "Index 219: -3.610583379836083\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import math\n",
    "\n",
    "def calculate_tnn(observation_dates, t):\n",
    "    tnn = None\n",
    "    min_diff = float('inf')\n",
    "    target_days = 10\n",
    "\n",
    "    for i in range(1, len(observation_dates)):\n",
    "        diff = (observation_dates[i] - observation_dates[t]).days\n",
    "        if diff > 0:\n",
    "            tnn_candidate = abs(target_days / diff - 1)\n",
    "            if tnn_candidate <= min_diff:\n",
    "                min_diff = tnn_candidate\n",
    "                tnn = i\n",
    "                \n",
    "    return tnn\n",
    "\n",
    "def calculate_return(observation_dates, t, tnn, risk_factor_values):\n",
    "    Dt = observation_dates[t]\n",
    "    Dtnn = observation_dates[tnn]\n",
    "    rj_Dt = risk_factor_values[t]\n",
    "    rj_Dtnn = risk_factor_values[tnn]\n",
    "\n",
    "    time_diff = (Dtnn - Dt).days\n",
    "    sqrt_days = math.sqrt(10 / time_diff)\n",
    "\n",
    "    return math.log(rj_Dtnn/rj_Dt) * sqrt_days\n",
    "\n",
    "def main():\n",
    "    timeseries_data = generate_random_time_series_data()\n",
    "    \n",
    "    observation_dates = timeseries_data['Date'].tolist()\n",
    "    risk_factor_values = timeseries_data['Value'].tolist()\n",
    "\n",
    "    returns = []\n",
    "    for t in range(len(observation_dates) - 1):\n",
    "        tnn = calculate_tnn(observation_dates, t)\n",
    "        return_10bd = calculate_return(observation_dates, t, tnn, risk_factor_values)\n",
    "        returns.append(return_10bd)\n",
    "\n",
    "    print(\"10-day business returns:\")\n",
    "    for i, return_10bd in enumerate(returns):\n",
    "        print(f\"Index {i}: {return_10bd}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "3792a15f-b413-4fe3-923b-3e04a9b18b9e",
   "metadata": {},
   "source": [
    "Explanation of the code:\n",
    "\n",
    "1. `calculate_tnn(observation_dates, t)`: This function calculates the index `tnn` that is \"nearest to 10 business days\" from the given date index `t`. It iterates over the observation dates and finds the index with the minimum difference in days from the target of 10 business days. The index `tnn` is then returned.\n",
    "\n",
    "2. `calculate_return(observation_dates, t, tnn, risk_factor_values)`: This function calculates the 10-business-days return using the provided formula. It takes the observation dates, date index `t`, index `tnn`, and risk factor values as inputs. It retrieves the risk factor values at the given indices and calculates the time difference in days between the observation dates. The formula is then applied to calculate the 10-business-days return, which is returned as the result.\n",
    "\n",
    "3. `main()`: This function serves as the entry point of the program. It generates the random time series data using the `generate_random_time_series_data` function. It then extracts the observation dates and risk factor values from the generated data. The user is prompted to enter the index `t` for which the 10-business-days return needs to be calculated. The `calculate_tnn` and `calculate_return` functions are called to calculate the return, and the result is printed to the console.\n",
    "\n",
    "By running the script and providing the required inputs, you can see the 10-business-days return for the given date index `t` based on the generated random time series data."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

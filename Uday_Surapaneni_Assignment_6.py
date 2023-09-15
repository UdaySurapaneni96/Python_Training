#!/usr/bin/env python
# coding: utf-8

import big_o

def two_sum_closest(nums, target):
    left = 0
    right = len(nums) - 1
    closest_sum = float('inf')

    while left < right:
        current_sum = nums[left] + nums[right]
        if abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return closest_sum

# Example usage
nums = [-2, 3, 7, 9, 11]
target = 13
closest_sum = two_sum_closest(nums, target)
print("Closest sum:", closest_sum)
positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(lambda n: two_sum_closest(n, target), positive_int_generator, n_repeats=100)
print(best)
for class_, residuals in others.items():
    print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))


def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    max_profit = 0
    buy_price = prices[0]
    
    for i in range(1, len(prices)):
        sell_price = prices[i]
        
        if sell_price > buy_price:
            profit = sell_price - buy_price
            max_profit += profit
        
        buy_price = sell_price
    
    return max_profit

# Example usage
prices = [7, 1, 5, 9, 6, 4]
profit = max_profit(prices)
print("Maximum profit:", profit)
positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(lambda n: max_profit(n), positive_int_generator, n_repeats=100)
print(best)
for class_, residuals in others.items():
    print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def find_twin_primes(n):
    twin_primes = []
    count = 0
    num = 2

    while count < 100:
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
            count += 1
        num += 1

    return twin_primes

# Example usage
twin_primes = find_twin_primes(100)
print("First 100 twin primes:")
for prime_pair in twin_primes:
    print(prime_pair)

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(find_twin_primes, positive_int_generator, n_repeats=100)
print("find_twin_primes:")
print("Best case time complexity:", best)
for class_, residuals in others.items():
    print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))



k = 0
j = 2
n = 100
for i in range(n // 2, n):
    for j in range(2, n, pow(2,j)):
            k = k + n / 2
print(k)

"""The time complexity of the given code can be analyzed as follows:
1.The outer loop runs from n // 2 to n, which means it iterates n - (n // 2) times. This can be simplified to n // 2 iterations.Hence the time complexity of outer loop is O(n)
2.The inner loop runs from 2 to n with a step size of pow(2, j). The value of j is initially set to 2 outside the loop. The inner loop will continue until j exceeds n.
3.The step size of the inner loop is pow(2, j), which means the value of j will be exponentially increasing with each iteration. The time complexity of inner loop is O(log(n))
4.Inside the inner loop, the statement k = k + n / 2 is executed. This statement has a constant time complexity of O(1).
5.To summarize, the time complexity of the given code can be approximated as O(n*log(n)),where n is the value of the variable n."""

value=0;
n=100;
for i in range(n):
    for j in range(i):
        value+=1
print(value)

"""The time complexity of the given code can be analyzed as follows:
1.The outer loop runs "n" times, and for each iteration of the outer loop, the inner loop runs "i" times. 2.Since the inner loop is nested inside the outer loop, the total number of iterations of the inner loop is the sum of the numbers from 1 to n-1, which is approximately (n^2)/2.
3.Therefore, the total number of iterations of the inner loop is proportional to n^2, resulting in a time complexity of O(n^2)."""
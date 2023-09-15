#!/usr/bin/env python
# coding: utf-8
#Q1
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        conjugate = ComplexNumber(other.real, -other.imaginary)
        numerator = self * conjugate
        denominator = other * conjugate
        real = numerator.real / denominator.real
        imaginary = numerator.imaginary / denominator.real
        return ComplexNumber(real, imaginary)

    def modulus(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            return f"{self.real:.2f}{self.imaginary:.2f}i"

# Read input
c_real, c_imaginary = map(float, input().split())
d_real, d_imaginary = map(float, input().split())

# Create complex numbers
C = ComplexNumber(c_real, c_imaginary)
D = ComplexNumber(d_real, d_imaginary)

# Perform operations
addition = C + D
subtraction = C - D
multiplication = C * D
division = C / D
mod_C = C.modulus()
mod_D = D.modulus()

# Print results
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(f"{mod_C:.2f}+0.00i")
print(f"{mod_D:.2f}+0.00i")


#Q2
"""class A:
    def function_A(self):
        print("This is function A in class A")

class B(A):
    def function_B(self):
        print("This is function B in class B")

class C(A,B):
    def function_C(self):
        print("This is function C in class C")

# MRO for class D with order C <- A, C <- B, and B <- A
print(C.mro())

# Create instances of class D
cobj = C()

# Call functions in each class
cobj.function_C()  # This is function C in class C
cobj.function_B()  # This is function B in class B
cobj.function_A()  # This is function A in class A"""

#Throws a type error "Cannot create a consistent method resolution
#order (MRO) for bases A, B",This is because of multilevel inheritance in which class C is derived from B which in turn is derived from A and hence C is indirectly derived from A.Hence class C can't be derived from A directly and the correct code is given by

class A:
    def function_A(self):
        print("This is function A in class A")

class B(A):
    def function_B(self):
        print("This is function B in class B")

class C(B):
    def function_C(self):
        print("This is function C in class C")

# MRO for class D with order C <- A, C <- B, and B <- A
print(C.mro())

# Create instances of class D
cobj = C()

# Call functions in each class
cobj.function_C()  # This is function C in class C
cobj.function_B()  # This is function B in class B
cobj.function_A()  # This is function A in class A

class X:
    def function_X(self):
        print("This is function X in class X")

class Y:
    def function_Y(self):
        print("This is function Y in class Y")

class Z:
    def function_Z(self):
        print("This is function Z in class Z")

class A(X, Y):
    def function_A(self):
        print("This is function A in class A")

class B(Y, Z):
    def function_B(self):
        print("This is function B in class B")

class M(A, B, Z):
    def function_M(self):
        print("This is function M in class M")

# MRO for class M with order M <- A, B <- A, X <- Y, Y <- Z, and object <- X, Y, Z
print(M.mro())

# Create instances of class M
m = M()

# Call functions in each class
m.function_M()  # This is function M in class M
m.function_A()  # This is function A in class A
m.function_B()  # This is function B in class B
m.function_X()  # This is function X in class X
m.function_Y()  # This is function Y in class Y
m.function_Z()  # This is function Z in class Z

#The MRO for this code starts from class M inheriting from classes A,B and Z so it first goes to A first then it was supposed to go to B but it goes to A parent X as it is derived from X and goes to class B instead of Y as Y is the common parent for both A and B so it took that part hence.The only plausible explanation would be that " child inherits from parent" and not vice versa and hence the MRO of the code is ambigous
#Q3
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: ${self.amount:.2f}")

    def deposit(self, amount):
        self.amount += amount
        print(f"Deposit of ${amount:.2f} successful.")
        self.display_balance()

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            print(f"Withdrawal of ${amount:.2f} successful.")
            self.display_balance()
        else:
            raise BalanceException("Insufficient balance. Withdrawal cannot be processed.")

    def transfer(self, amount, recipient):
        if self.amount >= amount:
            self.amount -= amount
            recipient.amount += amount
            print(f"Transfer of ${amount:.2f} to {recipient.name} successful.")
            print("Sender's Account:")
            self.display_balance()
            print("Recipient's Account:")
            recipient.display_balance()
        else:
            raise BalanceException("Insufficient balance. Transfer cannot be processed.")

class InterestRewardAcc(BankAccount):
    def __init__(self, name, amount):
        super().__init__(name, amount)

    def deposit(self, amount):
        self.amount *= 1.05
        self.amount += amount
        print(f"Deposit of ${amount:.2f} successful.")
        self.display_balance()

class SavingsAcc(InterestRewardAcc):
    def __init__(self, name, amount):
        super().__init__(name, amount)

    def withdraw(self, amount):
        if self.amount >= amount + 5:
            self.amount -= amount + 5
            print(f"Withdrawal of ${amount:.2f} successful. Service fee of $5 applied.")
            self.display_balance()
        else:
            raise BalanceException("Insufficient balance. Withdrawal cannot be processed.")

# Create InterestRewardAcc account
kevin = InterestRewardAcc("Kevin", 1000)
kevin.deposit(100)

# Create SavingsAcc account
john = SavingsAcc("John", 1000)
john.deposit(100)
john.withdraw(500)
john.transfer(500,kevin)

#Q4
class FormulaError(Exception):
    pass

def parse_input(user_input):
    elements = user_input.split()
    if len(elements) != 3:
        raise FormulaError("Invalid input. Please provide a formula with two numbers and an operator separated by spaces.")
    try:
        n1 = float(elements[0])
        n2 = float(elements[2])
    except ValueError:
        raise FormulaError("Invalid input. Please provide valid numbers.")
    op = elements[1]
    if op not in ['+', '-']:
        raise FormulaError("Invalid operator. Only addition (+) and subtraction (-) are supported.")
    return n1, op, n2

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2

# Start the calculator
while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    try:
        n1, op, n2 = parse_input(user_input)
        result = calculate(n1, op, n2)
        print(result)
    except FormulaError as e:
        print(f"Error: {str(e)}")







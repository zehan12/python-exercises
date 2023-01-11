# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call

def factorial(int):
    f = 1
    for i in range(int):
        f *= i+1
    print(f)

factorial(5)
#
# factorial(5)
#
# > 120
#

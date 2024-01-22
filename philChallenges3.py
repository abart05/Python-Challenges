# == EXERCISES ==


# Purpose: implements a childhood game
# Rules:   if the number is divisible by 3, return 'fizz'
#          if the number is divisible by 5, return 'buzz'
#          if the number is divisible by 15, return 'fizzbuzz'
#          otherwise, return the number
# Clue: you can check divisibility using modulo (%)
# Example:
#   Call:    fizz_buzz(3)
#   Returns: "fizz"
#   Call:    fizz_buzz(5)
#   Returns: "buzz"
#   Call:    fizz_buzz(15)
#   Returns: "fizzbuzz"
#   Call:    fizz_buzz(8)
#   Returns: 8

import math

def fizz_buzz(number):
    if number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 15 == 0:
        return "fizzbuss"
    else:
        return number

print(fizz_buzz(8))    

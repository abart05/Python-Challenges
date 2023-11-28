#First way using function
def factorial(n):
    factorial = 1 
    for i in range(n):
        factorial *= i + 1
    return factorial

print(factorial(4))

#second way using python built in math.factorial function
import math

num = int(input('Enter number: '))

output = math.factorial(num)
print('The factorial of number', num, 'is:',output)
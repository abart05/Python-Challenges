operator = input('''
Please type the math operation you wish to calculate: 
+ for addition, 
- for subtraction, 
* for mutlipilication, 
/ for division.
: ''')

num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))

def calculator(num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "You have not used a correct operator"

print("The Answer Is ", calculator(num1, num2))


# employees = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]

# for employee in employees:
#     pay = employee[1] * employee[2]
#     print(f"{employee[0]} has been paid £{pay:.2f}")

# total = 0
# count = 1

# for employee in employees:
#     total = total + employee[2]
#     count = count + 1

# average = total / count

# for employee in employees:
#     if employee[2] > average:
#         print(f"{employee[0]} is paid higher than the average employee")






for number in range(1,16):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


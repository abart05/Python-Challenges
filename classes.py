# class bank_account:
#     def __init__(self, name, balance, account_type, interest_rate):
#         self.name = name
#         self.balance = balance
#         self.account_type = account_type
#         self.interest_rate = interest_rate
#     def show_info(self):
#         print("Name: ", self.name)
#         print("Balance: ", self.balance)
#         print("Account Type: ", self.account_type)
#         print("Interest Rate: ", self.interest_rate)
#     def get_name(self):
#         print(self.name)
#     def set_name(self,name):
#         self.name = name
#     def get_balance(self):
#         print(self.balance)
#     def set_balance(self, balance):
#         self.balance = balance
#     def set_deposit(self, balance):
#         self.balance += balance
#     def set_withdraw(self, balance):
#         self.balance -= balance
        
# # andy_b = bank_account("Andy", 1000, "Savings", 4)
# # phil_h = bank_account("Phil", 3000, "Current", 3)
# # nicola_b = bank_account("Nicola", 0, "Savings", 5)
 

# # nicola_b.show_info()
# # nicola_b.set_deposit(350)
# # nicola_b.show_info()


# # andy_b.show_info()
# # andy_b.get_balance()
# # andy_b.set_deposit(3000)
# # andy_b.get_balance()
# # andy_b.show_info()
# # andy_b.set_withdraw(1500)
# # andy_b.show_info()
 
 
# #andy_b.show_info()
# #phil_h.show_info()
# #andy_b.get_name()



# # class Greeter():
# #     def __init__(self):
# #         print("Hello")

# # class Goodbye():
# #     def __init__(self):
# #         print("Goobye")
    
# # new = Greeter()
# # new1 = Goodbye()

# # class Footballer():
# #     def __init__(self, heading, speed, passing, striking):
# #         self.heading = heading
# #         self.speed = speed
# #         self.passing = passing
# #         self.striking = striking

# # footballer1 = Footballer(83, 23, 43, 46)
# # footballer2 = Footballer(82, 23, 43, 46)
# # footballer3 = Footballer(78, 34, 63, 82)
# # footballer4 = Footballer(5, 66, 77, 33)

# # print(f'Footballer1.speed: {footballer1.speed}')



# class Person():
#      def __init__(self, first_name, surname):
#          # note that we're not using instance variables here
#          self.first_name = first_name
#          self.surname = surname


#      def full_name(self):
#          # will this work without using instance variables above?
#          return f"{self.first_name} {self.surname}"


# alan_turing = Person("Alan", "Turing")
# print(alan_turing.full_name())
# # what gets returned here?



# class Superheros():
#     def __init__(self, name, power, secondPower, age):
#         self.name = name
#         self.power = power
#         self.secondPower = secondPower
#         self.age = age
#     def show_info(self):
#          print("Name: ", self.name)
#          print("Power: ", self.power)
#          print("Second Ability:", self.secondPower)
#          print("Age: ", self.age)
#     def can_sup_fly(self):
#         if self.power == "Flying":
#             return "This Superhero can fly"
#         else:
#             return "This Superhero cannot fly"
#     #     return f"This superhero {"can" if self.power == "Flying" else "cannot"} fly"
#     def change_super_power(self, power):
#         self.power = power





# sup1 = Superheros("Superman", "Flying", "Strong", 60)
# sup2 = Superheros("Spiderman", "WebShooting", "climbing", 19)
# sup3 = Superheros("Cyclops", "Lazer Beams","Intelligence", 22)
# sup4 = Superheros("Deadpool", "Immortal", "Gun", 101)

# sup2.show_info()
# # print(sup2.can_sup_fly())
# sup2.change_super_power("Swimming")
# sup2.show_info()



# Class name: StringFormatter
# Purpose: transforms strings
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: block_caps
#      Arguments: one, a string
#      Returns: the string in block caps
#   3. Name: lower_case
#      Arguments: one, a string
#      Returns: the string in lower case
# Example usage:
#   > string_formatter = StringFormatter()
#   > string_formatter.block_caps('hello')
#   'HELLO'
#   > string_formatter.lower_case('HELLO')
#   'hello'

# class StringFormater():
#     def __init__(self):
#         pass
#     def block_caps(self, string):
#         return string.upper()
#     def lower_case(self, string):
#         return string.lower()

# string_formatter = StringFormater()
# print(string_formatter.block_caps('hello'))
# print(string_formatter.lower_case('HELLO'))


class Employee():
    def __init__(self, firstName, surname, grade, location, startDate):
        self.firstName = firstName
        self.surname = surname
        self.grade = grade
        self.location = location
        self.startDate = startDate
    def change_first_name(self, firstName):
        self.firstName = firstName
    def change_surname(self, surname):
        self.surname = surname
    def fullname(self):
       return   "{} {}".format (self.firstName, self.surname)

employee1 = Employee("Andy", "Bart", "HEO", "Blackpool", "29/03/2016")


# employee1.change_first_name("Phil")
# print(employee1.fullname())
# employee1.change_surname("Hanlon")
# print(employee1.fullname())

# Class name: Cohort
# Purpose: represents a cohort
# Fields:
#   1. Name: name
#      Type: string
#      Purpose: the cohort name
#   2. Name: start_date
#      Type: Date
#      Purpose: the cohort start date
#   3. Name: end_date
#      Type: Date
#      Purpose: the cohort end date
# Methods:
#   1. Name: __init__
#      Arguments: one string representing a name,
#                 one string representing a start_date,
#                 one string representing an end_date
#   2. Name: calculate_duration
#      Arguments: none
#      Returns: the number of days between start_date and end_date
# Example usage:
#   > cohort = Cohort('June 2020', '2020-06-01', '2020-09-01')
#   > cohort.name
#   'June 2020'
#   > cohort.start_date
#   datetime.date(2020, 6, 1)
#   > cohort.end_date
#   datetime.date(2020, 9, 1)
#   > cohort.calculate_duration()
#   92

from datetime import date
class Cohort():
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)
    def calculate_duration(self):
        if self.start_date > self.end_date:
            return (self.start_date - self.end_date).days
        else:
            return (self.end_date - self.start_date).days
 
cohort = Cohort('June2020', '2020-06-01', '2020-09-01')
print(cohort.calculate_duration(), "days")



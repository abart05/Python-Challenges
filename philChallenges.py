# Purpose: return the string uppercase
# Example:
#   Call:    block_caps_a_string("hello world")
#   Returns: "HELLO WORLD"
def block_caps_a_string(string):
   string = string.upper()
   print(string)
   # your code goes here (delete the pass below)

#function call
#block_caps_a_string("Hello world")


# Purpose: return the string lowercase
# Example:
#   Call:    lower_case_a_string("HELLO WORLD")
#   Returns: "hello world"
def lower_case_a_string(string):
   string = string.lower()
   print(string)

#function call
#lower_case_a_string("HELLO WORLD")


# Purpose: return the length of the string
# Example:
#   Call:    length_of_a_string("hello")
#   Returns: 5
def length_of_a_string(string):
   x = string
   print(len(x))

#function call
#length_of_a_string("hello")


# Purpose: return the string reversed
# Example:
#   Call:    reverse_a_string("hello")
#   Returns: "olleh"
def reverse_a_string(string):
   string = string[::-1]
   print(string)

#function call
#reverse_a_string("hello")

#Example using loop
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

#function call
#reverse_a_string("hello loop")


# Purpose: return the string with uppercase swapped to lowercase and vice versa
# Example:
#   Call:    swap_the_case_of_a_string("Hello World")
#   Returns: "hELLO wORLD"
def swap_the_case_of_a_string(string):
   string = string.swapcase()
   print(string)

#function call
#swap_the_case_of_a_string("Hello World")


# Purpose: checks if the number given is odd
# Example:
#   Call:    is_integer_odd(1)
#   Returns: True
#   Call:    is_integer_odd(2)
#   Returns: False
def is_integer_odd(integer):
    x = integer
    if x % 2 != 0:
        print("True")
    else: 
        print("False")

#is_integer_odd(2)

# Purpose: checks if the number given is even
# Example:
#   Call:    is_integer_even(1)
#   Returns: False
#   Call:    is_integer_even(2)
#   Returns: True
def is_integer_even(integer):
    x = integer
    if x % 2 == 0:
        print("True")
    else: 
        print("False")

#is_integer_even(2)


# Purpose: converts an integer to a float
# Example:
#   Call:    integer_to_float(1)
#   Returns: 1.0
def integer_to_float(integer):
   x = integer
   print(float(x))

#integer_to_float(1)


# Purpose: converts an integer to a string
# Example:
#   Call:    integer_to_string(1)
#   Returns: "1"
def integer_to_string(integer):
   x = integer
   print(str(x))

#integer_to_string(1)


# Purpose: returns the integer one lower than the one given
# Example:
#   Call:    return_one_lower(4)
#   Returns: 3
def return_one_lower(integer):
   x = integer -1
   print(x)

#return_one_lower(4)


# Purpose: returns the integer one higher than the one given
# Example:
#   Call:    return_one_higher(4)
#   Returns: 5
def return_one_higher(integer):
   x = integer + 1
   print(x)

#return_one_higher(4)


# Purpose: rounds a float up to the nearest integer
# Example:
#   Call:    round_up(4.5)
#   Returns: 5
import math
def round_up(float):
   x = float
   print(math.ceil(x))

#round_up(4.5)

# Purpose: rounds a float down to the nearest integer
# Example:
#   Call:    round_down(4.5)
#   Returns: 4
def round_down(float):
   x = float
   print(math.floor(x))

#round_down(4.5)


# Purpose: converts a float to a string
# Example:
#   Call:    float_to_string(1.0)
#   Returns: "1.0"
def float_to_string(float):
   print(str(float))

#float_to_string(1.0)


# Purpose: converts a float to an integer
# Example:
#   Call:    float_to_integer(1.0)
#   Returns: 1
def float_to_integer(float):
   print(int(float))

#float_to_integer(1.0)



# Purpose: checks if a float is positive
# Example:
#   Call:    float_is_positive(1.0)
#   Returns: True
#   Call:    float_is_positive(-1.0)
#   Returns: False
def float_is_positive(float):
   if float >= 0:
        print("True")
   else:
        print("False")

#float_is_positive(-1.0)


# Purpose: checks if a float is negative
# Example:
#   Call:    float_is_negative(1.0)
#   Returns: False
#   Call:    float_is_negative(-1.0)
#   Returns: True
def float_is_negative(float):
   if float <= 0:
        print("True")
   else:
        print("False")

#float_is_negative(-1.0)


# Purpose: converts a boolean to a string
# Example:
#   Call:    boolean_to_string(True)
#   Returns: "True"
def boolean_to_string(boolean):
   print(bool(boolean))
   

#boolean_to_string("True")

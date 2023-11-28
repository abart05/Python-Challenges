# shopping_list = ['apple', 'jam', 'eggs', 'milk', 'bread']


# shopping_list.append('crisps')

# shopping_list[0]='peaches'

# del shopping_list[1]

# print(shopping_list)

# print(len(shopping_list))

# shopping_list2 = ['pens', 'oranges','berries']

# print(len(shopping_list + shopping_list2))

# sen1 = "I love pizza"
# print(sen1[3])


# def plus_ten(a):
#     return a + 10

# print(plus_ten(2))

def convert_to_rom(x):
    # Lists for mapping
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    # Initialize variables
    i = 12
    roman_numeral = ""

    # Main conversion loop
    while x != 0:
        # Print the current state
        print(f"x: {x}, current number: {numbers[i]}, current Roman numeral: {roman[i]}")

        # Check if the current number can be subtracted from x
        if numbers[i] <= x:
            # Append the corresponding Roman numeral
            roman_numeral += roman[i]
            # Subtract the number from x
            x = x - numbers[i]
            print(f"Added {roman[i]} to the result, new x: {x}")
        else:
            # Move to the next smaller number
            i -= 1
            print(f"Current number too large, moving to the next smaller number, new index i: {i}")

    # Print the final result
    print(f"Final Roman numeral: {roman_numeral}")

    # Return the constructed Roman numeral
    return roman_numeral

# Example usage
print(convert_to_rom(4365))

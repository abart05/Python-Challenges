# Exercise 1 - Radian to degrees

def radian_to_degrees(user):
    convert = user * (180/3.14159265)
    return f"This is {convert:.2f} degrees"

# print(radian_to_degrees(2))

# Exercise 2 - sort a list

def sort_list(x, y):
    if y == "asc":
        x.sort()
        return x
    elif y == "desc":
        x.sort(reverse = True)
        return x
    elif y == "none":
        return x
    else:
        return x

def sort_list2(x, y):
    match y:    
        case "asc":
            sorted(x)
            return x
        case "desc":
            print(x)
            x.sort(reverse = True)
            return x
        case "none":
            return x
        case _ :
            print("invalid action")

# list1 = input("please input numbers: ")
# list3 = list1.split()
# list2 = input("Please input: 'asc', 'desc', 'none': ")

# print(sort_list2(list3, list2))


# Exercise 3 -  Convert decimal numbers into a binary

# user = input("Please inser a number: ")

# def convert_to_binary(user):
#     z = bin(user)[2:]
#     return f" The binary number is: {z}"

# print(convert_to_binary(7))

#  Exercise 4 - Count Vowels in a string

# user = input("Please input a string:")

# def count_vowels(string):
#     count = 0
#     vowels = "aeiou"
#     for i in string.lower():
#         if i in vowels: 
#             count += 1
#     return f"This string contains {count} vowels."
    
# print(count_vowels(user))
    
    
# Exercise 5 - Hide Credit Card number 


def hide_credit_card(string):
    displaycharacters = 4
    lenghtOfString = len(string)
    print(lenghtOfString)
    i = 0
    blankstring = ""
    for i in range(lenghtOfString):
        if i >= (lenghtOfString - displaycharacters):
            blankstring += string[i]
        else:
            blankstring += "*"
    return blankstring

user = input("Input Credit Card: ")

output = hide_credit_card(user)
print(output)


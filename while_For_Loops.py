# # while loops

# # number = 0

# # while number < 5:
# #     number = number + 1
# #     if number == 3:
# #         continue # can use break as well 
# #     print(number)

# # else:
# #     print("no longer less than 5")


# # for loop 

# integers = [1, 2, 3, 4, 5]

# # for number  in integers:
#     # print(number)


# ice_cream_dict = {'name': 'Andy Bart', 'Weekly intake': 5, 'fav ice cream': ['Vanilla', 'chocolate chip']}

# # for key, value in ice_cream_dict.items():
# #     print(key, '->', value)

# #nested for loop

# flavours = ['vanilla', 'chocolate', 'cookie dough']
# toppings = ['hot fudge', 'oreos', 'choc chip']

# for one in flavours:
#     for two in toppings:
#         print(one, "topped with ", two)
                                                                        

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"your number is {num}")

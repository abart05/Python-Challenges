def time_convert(to_convert):
    hours = int(to_convert/60)
    minutes = to_convert - (60 * hours)
    return str(hours) + ':' + str(minutes)

print('Enter a whole number to return hours and minutes in H:M format')
print('Result:', time_convert(int(input('Enter number: '))))
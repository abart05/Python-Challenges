# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

def manage_time(x, i):
    words = int(x)
    words_per_minute = int(i)
    reading_time_minutes = words / words_per_minute
    minutes, seconds = divmod(reading_time_minutes * 60, 60)
    return int(minutes), int(seconds)


text = "2500"
words_per_min = 300

minutes, seconds = manage_time(text)
print(f"Reading Time: {minutes} minutes and {seconds} seconds")


import math
def reading_time (mynum_words, myreading_speed):
    if str(mynum_words).isnumeric() == False:
        return "cannot work this out"
    if str(myreading_speed).isnumeric() == False:
        return "cannot work this out"
    mynum_words = int(mynum_words)
    myreading_time = (mynum_words / myreading_speed)
    mynumberofseconds, mynumberofmins = math.modf(myreading_time)
    mynumberofseconds = int(60 * mynumberofseconds)
    mynumberofmins = int(mynumberofmins)
    myreturn = str(mynum_words) + ' words will take ' + str(mynumberofmins) + ' minutes and ' + str(mynumberofseconds) + ' seconds to read.'
    myreturn = str(mynumberofmins) + 'mins ' + str(mynumberofseconds) + 'seconds'
    return(myreturn)

print(reading_time(2500, 500))

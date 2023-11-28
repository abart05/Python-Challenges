sentence = 'United never get any decisions from VAR'

constCount = 0 
for i in range(0,len(sentence)):
    if (sentence[i] == 'a' or sentence[i] == 'A' or sentence[i] == 'e' or sentence[i] == 'E' or sentence[i] == 'i' or sentence[i] == 'I' or sentence[i] == 'o' or sentence[i] == 'O' or sentence[i] == 'u' or sentence[i] == 'U'):
        constCount = constCount + 1
print('Constant Count = ', constCount)
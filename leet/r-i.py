# Roman-to-Integer

roman_ints = {
'I': 1,
'V': 5,
'X': 10,
'L': 50,
'c': 100,
'D': 500,
'M': 1000,
}

x = 'IV'

total = 0
for char in x:
    if char in roman_ints.keys():
        if char == 'I' and char[char + 1] == 'V': # char == 'X' and char == 'C'
            i = 4
        elif char == 'V' and char[char - 1] == 'I':
            continue
        elif char =='I' and char[char + 1] == "X":
            i = 9

        else:
            i = roman_ints[char]
            total += i
else:
    print(total)
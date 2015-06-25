#!/usr/bin/python3

numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'M': 1000,
}

#test
def parseRoman(text):
    result = 0
    counter = 0

    for i in text:
        value = numerals[i]

        if counter + 1 < len(text):
            next = numerals[text[counter + 1]]
        else:
            next = numerals[text[counter]]
        operator = -1 if next > value else 1

        counter += 1
        result += operator * value

    return result

print(parseRoman("IV"))
print(parseRoman("XX"))
print(parseRoman("MCMLVII"))

#!/usr/bin/python3

numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'M': 1000,
}

def parseRoman(text):
    result = 0
    counter = 0

    for i in text:
        value = numerals[i]
        operator = 1 if numerals[text[counter + 1]] > value else -1

        counter += 1 if counter < len(text) else 0
        result += operator * value

    return result

test = "IV"

print(parseRoman(test))

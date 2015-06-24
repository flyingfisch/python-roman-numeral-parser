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
    j = 1
    for i in text:
        value = numerals[i]
        operator = 1 if numerals[text[j]] > value else -1

        j++

test = "IV"

print(parseRoman(test))

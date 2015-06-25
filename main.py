#!/usr/bin/python3

import sys

# Put the command line input in a var
input = sys.argv[1]

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

    # cycle through the digits in the roman numeral
    for i in text:
        # Get the value of the roman numeral
        value = numerals[i]

        # if counter + 1 is less than the length of the string, check the next digit to decide whether to subtract this number from the total or to add it
        if counter + 1 < len(text):
            next = numerals[text[counter + 1]]
        else:
            next = numerals[text[counter]]

        operator = -1 if next > value else 1

        # increment counter, add the value of this digit to the total
        counter += 1
        result += operator * value

    return result

# calculate the result
# TODO: set this up so it does not run if imported as a module
print(parseRoman(input))

# some tests
#print(parseRoman("IV"))
#print(parseRoman("XX"))
#print(parseRoman("MCMLVII"))

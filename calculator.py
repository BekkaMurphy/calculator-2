"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
print """
    Welcome to calculator.  Please enter a calculation by inputting the
    operation followed by operand(s).
    To quit, press 'q'
"""

def tokenize_input():
    """ Asks for user input and tokenizes input """

    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    if len(tokens) >= 2:
        operation = tokens[0]
        operand1 = tokens[1:]
        if len(tokens) == 3:
            operand2 = float(tokens[2])

# calculate()

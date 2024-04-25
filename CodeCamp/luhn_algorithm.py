"""The Luhn algorithm.

The Luhn Algorithm is widely used for error-checking in various
applications, such as verifying credit card numbers.

The Luhn algorithm, also known as the modulus 10 or mod 10 algorithm,
is a simple checksum formula used to validate a variety of 
identification numbers, such as credit card numbers, IMEI numbers,
Canadian Social Insurance Numbers...
"""

# https://www.freecodecamp.org/learn/scientific-computing-with-python/
# https://en.wikipedia.org/wiki/Luhn_algorithm
# https://www.geeksforgeeks.org/luhn-algorithm/

# The Luhn algorithm is as follows:

#     From the right to left, double the value of every second digit;
#     if the product is greater than 9, sum the digits of the products.
#     Take the sum of all the digits.
#     If the sum of all the digits is a multiple of 10, then the number
#     is valid; else it is not valid.

# Assume an example of an account number "7992739871" that will have a
# check digit added, making it of the form 7992739871x:

# Account number      7   9  9  2  7  3  9   8  7  1  x
# Double every other  7  18  9  4  7  6  9  16  7  2  x
# Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x

import os


def verify_card_number(card_number):
    """The Luhn algorithm.
    A Luhn algorithm is used to verify credit card numbers or other
    identification numbers, such as Aadhaar number.
    """
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits

    return total % 10 == 0


def int_validation(value) -> int:
    """This Function tests if an inputted value may belong 
    to <class 'int'> and be a zero or positive integer. 
    If not, then it asks to repeat Input.
    """
    # Pre-cleaning. Removing "-" and " " from the Input:
    value_translation = str.maketrans({'-': '', ' ': ''})
    value = value.translate(value_translation)

    try:
        value = int(value)
    except:
        value = input('ERROR: Only integer numbers are allowed. \
\nRepeat Input: ')
        value = int_validation(value)  # Recursion!
#     else:
#         if value < 0:
#             value = input('ERROR: Only integer numbers >= 0  \
# are allowed.\nRepeat Input: ')
#             value = int_validation(value)  # Recursion!
#         else:
#             pass
    finally:
        return value


def luhn_algorithm():
    """Luhn algorithm - main function."""

    os.system('cls')  # Clearing the Screen.
    # The Greeting.
    print('\nHello Host!\nYou run version 01.02 of \
the program luhn_algorithm.py.')

    # The main loop:
    k = 'continue'
    while k not in ['q', 'Q']:
        # The Data Input:
        card_number = input('\nInput Card Number: ')

        # The Pre-Validation:
        # Only positive integers are allowed in the Card Number.
        card_number = str(int_validation(card_number))

        # The Call & Output block (if True, then VALID!):
        if verify_card_number(card_number):
            print('VALID!')
        else:
            print('INVALID!')

        # The end of the main loop.
        k = input('\nWould you like to input another \
Card Number? \n(Press "q" to exit, or "ENTER" to continue): ')

    input('Press "ENTER" to exit luhn_algorithm.py: ')  # Exit.
    return


if __name__ == "__main__":
    luhn_algorithm()

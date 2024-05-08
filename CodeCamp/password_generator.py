"""The Password Generator."""

# In this project, we'll learn how to import modules from the
# Python standard library. We'll also learn how to use Regular
# Expressions by building our own password generator program.

# A regular expression, or regex, is a pattern used to match a
# specific combination of characters inside a string. It is a
# valid alternative to if/else conditional statements when we
# need to match or find patterns inside a string for validation
# purposes, character replacement, and others.

# The compile() function from the re module compiles the string
# passed as the argument into a regular expression object that
# can be used by other re methods.

# The search() function from the re module analyzes the string
# passed as the argument looking for the first place where the
# regex pattern matches the string.
# ...
# The [0-9] class is equivalent to \d, the [^0-9] class is
# equivalent to \D. Alphanumeric characters can be matched with
# \w and non-alphanumeric characters can be matched with \W.

# https://www.freecodecamp.org/learn/scientific-computing-with-python/
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html
# https://developers.google.com/edu/python/regular-expressions
# https://www.geeksforgeeks.org/regular-expression-python-examples/
# https://www.w3schools.com/python/python_regex.asp
# https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/

import os
import re
import secrets
import string
import time


def generate_password(
    length=16,
    nums=1,
    special_chars=1,
    uppercase=1,
    lowercase=1
):
    """The Usage Regular Expressions to building our own
    password generator program.
    """
    # The Defining the possible characters for the password:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


def pre_cleaning(string_to_check) -> str:
    """This Function checks the Input (string_to_check) and,
    if there are not eligible symbols in it, removes those
    (replace on '').
    """
    string_to_check = str(string_to_check)  # Convert to <class 'str'>.

    # Replace "-", " " and "\t" on "" in the Input:
    value_translation = str.maketrans(
        {
            '-': '',
            ' ': '',
            '\t': ''
        }
    )
    result_string = string_to_check.translate(value_translation)

    if len(result_string) < len(string_to_check):
        print('WARNING: Some not eligible symbols were removed \
from the Input!')
    else:
        pass

    return result_string


def int_validation(value, min_value=0) -> int:
    """This Function tests if an Input (value) may belong 
    to <class 'int'> and be a positive integer >= min_value. 
    If not, then it asks to repeat Input.
    """
    # # Pre-cleaning. Removing "-", "\t" and " " from the Input:
    value = pre_cleaning(value)

    try:
        value = int(value)
    except:
        value = input('ERROR: Only decimal digits \
[0,1,2,3,4,5,6,7,8,9] are allowed. \nRepeat Input: ')
        value = int_validation(value, min_value)  # Recursion!
    else:
        if value < min_value:
            value = input(f'ERROR: Only integer numbers >= {min_value}  \
are allowed.\nRepeat Input: ')
            value = int_validation(value, min_value)  # Recursion!
        else:
            pass
    finally:
        return value


def password_generator():
    """Password Generator - the main function."""

    os.system('cls')  # Clearing the Screen.

    # The Greeting.
    print('\nHello Host!\nYou run the version 01.01 of \
the program password_generator.py.')

    # The main loop:
    while True:

        # The Data Input:
        password_length = input('\nInput password\'s length: ')

        # Input Validation:
        password_length = int_validation(password_length, 6)

        generated_password = generate_password(password_length)
        print('\nThe generated Password is: ', generated_password)

        # The end of the main loop.
        _ = input('\nWould you like to generate another \
password? \n(Press "ENTER" to continue, or "q" to exit): ')
        if _ in ['q', 'Q']:
            break

    return print('Good JOB!')


if __name__ == '__main__':
    password_generator()
    time.sleep(2)

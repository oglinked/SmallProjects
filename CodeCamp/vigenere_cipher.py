"""Vigenère cipher.
Learn String Manipulation by Building a Cipher.
"""

# https://www.freecodecamp.org/learn/scientific-computing-with-python/
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# https://www.geeksforgeeks.org/vigenere-cipher/

import os


def vigenere(message, key, direction=1):
    """Vigenère cipher function.
    
    The Vigenère cipher (French pronunciation: [viʒnɛ:ʁ]) is
    a method of encrypting alphabetic text where each letter
    of the plaintext is encoded with a different Caesar cipher,
    whose increment is determined by the corresponding letter
    of another text, the key.
    
    Parameters:
        message     - the text to encrypt/decrypt;
        key         - the key for encrypt/decrypt;
        direction   =  1       encrypt action;
                    = -1       decrypt action.
    """
    
    # Initializing variables:
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message:
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode:
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    """The function to call encryption."""
    return vigenere(message, key)


def decrypt(message, key):
    """The function to call decryption."""
    return vigenere(message, key, -1)


def vigenere_cipher():
    """Vigenère cipher - main function"""

    os.system('cls')  # Clearing the Screen.
    # The Greeting.
    print('\nHello Host!\nYou run version 01.01 of \
the program vigenere_ciper.py.')

    # The main loop:
    k = 'continue'
    while k not in ['q', 'Q']:
        # The Data Input:
        action = input('\nInput "1" for encrypt, or "-1" for decrypt: ')
        text = input('Input the text: ')
        custom_key = input('Input the key to encrypt/decryot: ').lower()

        # The call & Output block:
        if action == "1":
            print(f'\nText: {text}')
            print(f'Key: {custom_key}')
            encryption = encrypt(text, custom_key)
            print(f'\nEncrypted text: {encryption}\n')
        else:
            print(f'\nEncrypted text: {text}')
            print(f'Key: {custom_key}')
            decryption = decrypt(text, custom_key)
            print(f'\nDecrypted text: {decryption}\n')

        # The end of the main loop.
        k = input('\nWould you like to take another \
encrypt/decrypt action? \n(Press "q" to exit, or "ENTER" to continue): ')

    input('Press "ENTER" to exit vigenere_cipher.py: ')  # Exit.
    return


if __name__ == "__main__":
    vigenere_cipher()

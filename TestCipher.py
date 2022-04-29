
#  Description: This program uses input from a file to encode and decode text using the Rail Fence Cipher and the Vigenere Cipher.

import sys, math, string

# returns a single string that is encoded with rail fence algorithm
def rail_fence_encode ( strng, key ):
    encoded_lst = [['' for i in range(len(strng))] for j in range(key)]

    x = 0
    y = 0
    increment = 1
    
    for i in range(len(strng)):

        # switches increment direction
        if x >= key - 1:
            increment = -1
        if x == 0:
            increment = 1

        encoded_lst[x][y] = strng[i]
        
        x += increment
        y += 1

    encoded_string = ''

    # concatenates lst of letters
    for lst in encoded_lst:
        for char in lst:
            if char != '':
                encoded_string += char

    return encoded_string

#  function returns a single string that is decoded with rail fence algorithm
def rail_fence_decode ( strng, key ):

    lst =  [[" " for i in range(len(strng))] for j in range(key)]
    row = 0
    col = 0
    increment = 1
    num_row = -1
    letter_index = 0
    # outer loop which loops for every row in the 2d list
    for j in range(key):
        num_row += 1
        row = num_row
        col = num_row
        # inner loop which loops for every letter in string
        # places letter in only row 0 until end of row is reached, then moves on to row 1 etc.
        for i in range(len(strng)):
            if col >= len(strng):
                break
            if row == 0:
                increment = 1
            if row == key - 1:
                increment = - 1
            if row == num_row:  
                lst[row][col] = strng[letter_index]
                letter_index += 1
            row += increment
            col += 1   
    # section of method which decodes letters given in 2d list 
    row = 0
    col = 0
    increment = 1
    result = ""
    # for every letter in string, loops through filled 2d list diagonally to decode word
    for i in range(len(strng)):
        if row == 0:
            increment = 1
        if row == key - 1:
            increment = - 1
        result += lst[row][col]
        row += increment
        col += 1
    return result

# function converts all characters to lower case and then removes all digits, punctuation marks, and spaces. s
def filter_string ( strng ):
    
    strng = strng.lower()
    result = ""
    for letter in range(len(strng)):
        if not (strng[letter].isdigit()) and strng[letter] not in string.punctuation and strng[letter] != ' ':
            result += strng[letter]

    return result	

def encode_character (p, s):

    difference = abs(ord(p) - 97)
    
    # resets difference to account for the end of the alphabet
    if difference + ord(s) > 122:
        new_difference = (difference + ord(s)) - 122
        letter = chr(96 + new_difference)
    else:
        letter = chr(difference + ord(s))

    return letter

def decode_character (p, s):

    difference = abs(ord(p) - 97)

    # resets difference to account for the beginning of the alphabet
    if ord(s) - difference < 97:
        new_difference = (97 - (ord(s) - difference))
        letter = chr(123 - new_difference)
    else:
        letter = chr(ord(s) - difference)
        
    return letter	

def vigenere_encode ( strng, phrase ):

    # filters strng
    new_strng = filter_string(strng)

    # multiplies pass phrase to same length of strng
    multiple = math.ceil(len(new_strng) / len(phrase))
    phrase *= multiple
    password = phrase[0: len(new_strng)]

    encrypted_strng = ''

    # encodes each character and adds to a new string
    for i in range(len(new_strng)):
        letter = encode_character(password[i], new_strng[i])
        encrypted_strng += letter
    
    return encrypted_strng

def vigenere_decode ( strng, phrase ):

    # filters strng
    new_strng = filter_string(strng)

    # multiplies pass phrase to same length of strng
    multiple = math.ceil(len(new_strng) / len(phrase))
    phrase *= multiple
    password = phrase[0: len(new_strng)]

    decrypted_strng = ''

    # decodes each character and adds to a new string
    for i in range(len(new_strng)):
        letter = decode_character(password[i], new_strng[i])
        decrypted_strng += letter
    
    return decrypted_strng  

def main():

    # encrypt and print the encoded text using rail fence cipher
    rf_plain_text = sys.stdin.readline().strip()
    rf_encode_key = int(sys.stdin.readline().strip())

    print("Rail Fence Cipher")
    print()
    print("Plain Text: " + rf_plain_text)
    print("Key:", rf_encode_key)
    print("Encoded Text: " + rail_fence_encode(rf_plain_text, rf_encode_key))
    print()

    # decrypt and print the plain text using rail fence cipher
    rf_encoded_text = sys.stdin.readline().strip()
    rf_decode_key = int(sys.stdin.readline().strip())

    print("Encoded Text: " + rf_encoded_text)
    print("Enter Key:", rf_decode_key)
    print("Decoded Text: " + rail_fence_decode(rf_encoded_text, rf_decode_key))
    print()
    
    # encrypt and print the encoded text using Vigenere cipher
    vc_plain_text = sys.stdin.readline().strip()
    vc_encode_pass = sys.stdin.readline().strip()

    print("Vigenere Cipher")
    print()
    print("Plain Text: " + vc_plain_text)
    print("Pass Phrase: " + vc_encode_pass)
    print("Encoded Text: " + vigenere_encode(vc_plain_text, vc_encode_pass))
    print()

    # decrypt and print the plain text using Vigenere cipher
    vc_encoded_text = sys.stdin.readline().strip()
    vc_decode_pass = sys.stdin.readline().strip()

    print("Encoded Text: " + vc_encoded_text)
    print("Pass Phrase: " + vc_decode_pass)
    print("Decoded Text: " + vigenere_decode(vc_encoded_text, vc_decode_pass))
    
if __name__ == "__main__":
  main()

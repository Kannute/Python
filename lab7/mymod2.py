import string

alphabet = string.ascii_letters  


def caesar_encryption(filename, shift): 
    '''
    Function for Ceasar encryption of a given file. 
    Creates a new file "Encrypted.txt".
    Returns encrypted text.
    '''
    cipherText = ""

    with open(filename,'r', encoding = 'utf-8') as f:
        plainText = f.read()
        for ch in plainText:
            if ch.isalpha():
                alphabet = ord(ch) + shift 
                if alphabet > ord('z'):
                    alphabet -= 26
                finalLetter = chr(alphabet)
                cipherText += finalLetter
    newfile = open("Encrypted.txt" , 'w')
    newfile.write(cipherText)
    newfile.close()
    return cipherText



def ceasar_decryption(filename, shift):
    '''
    Function to decrypt a given file
    '''
    decipheredText = ""
    with open(filename,'r', encoding = 'utf-8') as f:
        cipherText = f.read()
    
        for c in cipherText:

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - shift) % len(alphabet)
                new_character = alphabet[new_position]
                decipheredText += new_character
            else:
                decipheredText += c
    newfile = open("Decrypted.txt", 'w')
    newfile.write(decipheredText)
    return decipheredText


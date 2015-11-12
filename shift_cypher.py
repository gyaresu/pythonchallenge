import string
import sys

text = raw_input("What are you trying to decode?")
num = int(raw_input("How many characters is it shifting to the right?"))

def shift(text, num):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[num:] + alphabet[:num]
    table = string.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

print shift(text,num)

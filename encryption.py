import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation
all_chars = upper + lower + digits + symbols + ' '

def reverse_encryption(input_pw):
    pw_cipher = input_pw[::-1]
    return pw_cipher

def reverse_decryption(input_cipher):
    pw_plaintext = input_cipher[::-1]
    return pw_plaintext

def caesar_encryption(input_pw, cae_key):
    cae_cipher = ''
    size_char = len(all_chars)
    for i in input_pw:
        if i in all_chars:
            num = all_chars.find(i)
            num_new = (num + cae_key)%size_char
            cae_cipher = cae_cipher + all_chars[num_new]
    return cae_cipher

def caesar_decryption(input_cipher, cae_key):
    cae_plain = ''
    size_char = len(all_chars)
    for i in input_cipher:
        if i in all_chars:
            num = all_chars.find(i)
            num_new = (num - cae_key)%size_char
            cae_plain = cae_plain + all_chars[num_new]
    return cae_plain
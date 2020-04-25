import random

message = input("enter the message:\t")
code = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*(){}|:<>-_=+/*";?.,'
# random key genration
key = random.randint(10, 90)


# encryting message
def encrypt_data(message, key):
    global encrypt
    encrypt = ''
    global k
    message = message + str(key)
    for i in message:
        if i != ' ':
            position = code.find(i)
            newposition = (position + key) % 91
            encrypt += code[newposition]
        else:
            encrypt += ' '
    print('Encryted data is: ', encrypt)
    k = encrypt[-2] + encrypt[-1]


# calling encrytion function
encrypt_data(message, key)


# decrypting key
def key_decrypt(k, key):
    global key1
    key1 = ''
    for i in k:
        position = code.find(i)
        newposition = (position - key) % 91
        key1 += code[newposition]


# calling decryting key function
key_decrypt(k, key)


# message=input("enter the message:\t")
def decrypt_data(encrypt, key1):
    global d
    decrypt = ''
    for i in encrypt:
        if i != ' ':
            position = code.find(i)
            newposition = (position - key1) % 91
            decrypt += code[newposition]
        else:
            decrypt += ' '
    d = decrypt[:-2]
    print('Decryted data is: ', d)


# calling decrytion function
decrypt_data(encrypt, key)

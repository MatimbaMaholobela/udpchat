#from ast import pattern
import string 
import random

class Encyption:

    global chars
    chars = list(" "+string.digits + string.punctuation + string.ascii_letters)
    global keys 
    keys =string.punctuation+string.digits+ " "+ string.ascii_letters

    """
        encypt is a function that takes a message and list that contains they encyption code
        with the key for the encyption

    """
    def encypt(message):

        cipher=""
        for i in message:
            index = chars.index(i)
            cipher  += keys[index]
        return cipher

    """
        dencyption is a function that takes a list of encytion code and keys then dencypt the message
    """
    def dencypt(cipher):

        message=""
        for j in cipher:
            index = keys.index(j)
            message+=chars[index]
        return message

    global encypt_code
    encypt_code = list(string.punctuation+string.digits+string.ascii_letters+" ")
    global M
    M =20
    global size
    size = len(encypt_code)
    print(size)

    def cipher(msg):
        cipher = ""

        for i in msg:
            for j in range(size):
                if (i==encypt_code[j]):
                    cipher+=encypt_code[(j+M)%size]
        return cipher
    
    def decipher(msg):
        
        decipher = ""

        for i in msg:
            for j in range(size):
                if(i==encypt_code[j]):

                    """

                    """
                    if(j-M)<=0:

                        decipher+=encypt_code[(size+(j-M))%size]

                    else:
                        decipher+=encypt_code[abs((j-M)%size)]
        return decipher



        
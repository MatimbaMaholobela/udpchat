import string 
import random

class Encyption:

    global chars
    chars = list(" "+string.digits + string.punctuation + string.ascii_letters)
    global keys 
    keys = chars.copy()

    """
        encypt is a function that takes a message and list that contains they encyption code
        with the key for the encyption

    """
    def encypt(message):

        random.shuffle(keys)
        cipher=""
        for i in message:
            index = chars.index(i)
            cipher  += keys[index]
        return (cipher,keys)

    """
        dencyption is a function that takes a list of encytion code and keys then dencypt the message
    """
    def dencypt(arr):

        message=""
        for j in arr[0]:
            index = arr[1].index(j)
            message+=chars[index]
        return message
        
    #dencypt(encypt(message))
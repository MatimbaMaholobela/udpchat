import string 
import random
from socket import *

chars = list(" "+string.digits + string.punctuation + string.ascii_letters)
keys = chars.copy()

message ="Matimba Maholobela"

def encypt(message):
    
    random.shuffle(keys)
import random
import os
import time

def limparTela():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def RNG(a,b):
    return random.randint(a,b)

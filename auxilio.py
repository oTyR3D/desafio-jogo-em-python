import random
import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def RNG():
    return random.randint(1, 100)

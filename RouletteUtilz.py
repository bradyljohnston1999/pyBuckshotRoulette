import os


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


class Colors:
    WHITE = '\033[97m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'

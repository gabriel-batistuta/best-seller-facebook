# from colorama import Fore, Style
from colorama import Fore, Style

def red(text):
    return f"{Fore.RED}{text}{Fore.RESET}"

def green(text):
    return f"{Fore.GREEN}{text}{Fore.RESET}"

def blue(text):
    return f"{Fore.BLUE}{text}{Fore.RESET}"

def yellow(text):
    return f"{Fore.YELLOW}{text}{Fore.RESET}"

def cyan(text):
    return f"{Fore.CYAN}{text}{Fore.RESET}"

def magenta(text):
    return f"{Fore.MAGENTA}{text}{Fore.RESET}"

def white(text):
    return f"{Fore.WHITE}{text}{Fore.RESET}"

def black(text):
    return f"{Fore.BLACK}{text}{Fore.RESET}"

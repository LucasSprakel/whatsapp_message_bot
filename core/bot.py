import pywhatkit
import time 
from colorama import init, Fore
import os
import sys


init()

contatos = []
message = ""
var_key = ""


def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def add_numbers():
    while True:
        numero = str(input(Fore.MAGENTA + 'Enter phone number: '))
        contatos.append(numero)
        num_continue = str(input('Do you want to add another number?(y)es or (n)o: '))
        if num_continue == 'y':
            continue
        elif num_continue == 'n':
            break
        else:
            print(Fore.RED + 'Message_bot Error: Invalid Char\n')


def show_numbers():
    if len(contatos) == 0:
        print(Fore.YELLOW + 'Message_bot Warning: You need to add a number\n')
    else:
        for num in contatos:
            print(Fore.MAGENTA + f'Number {contatos.index(num)+1}: {num}\n')
    global var_key 
    var_key = str(input('Press ENTER to continue'))   


def write_message():
    global message 
    message = str(input(Fore.MAGENTA + 'Write the message you want to send: '))


def show_message():
    if message == "":
        print(Fore.YELLOW + 'Message_bot Warning: Write a message first\n')
    else:
        print(Fore.MAGENTA + f'Your message: {message}\n')
    global var_key 
    var_key = str(input('Press ENTER to continue'))
        

def send_message(number_of_messages=1):
    while len(contatos) >= 1:
        i = 0
        print(Fore.MAGENTA + f"Sending '{message}' for the following number: {contatos[0]}")
        while i < number_of_messages:
            try:
                pywhatkit.sendwhatmsg_instantly(contatos[0], message, 60, True, 5)
            except pywhatkit.core.exceptions.CountryCodeException:
                print(Fore.RED + f'Message_bot Error: {contatos[0]} is a Invalid Number')
                exit(1)
            i += 1
        del contatos[0]
        time.sleep(10)


def credits():
    print(Fore.MAGENTA +
            """       
                         ____        
                        | __ ) _   _ 
                        |  _ \| | | |
                        | |_) | |_| |
                        |____/ \__, |
                               |___/ 
 _                          ____                  _        _ 
| |   _   _  ___ __ _ ___  / ___| _ __  _ __ __ _| | _____| |
| |  | | | |/ __/ _` / __| \___ \| '_ \| '__/ _` | |/ / _ \ |
| |__| |_| | (_| (_| \__ \  ___) | |_) | | | (_| |   <  __/ |
|_____\__,_|\___\__,_|___/ |____/| .__/|_|  \__,_|_|\_\___|_|
                                 |_|      
        
        
        """)
    global var_key 
    var_key = str(input('Press ENTER to continue'))


def help():
    print(Fore.MAGENTA +
        """
Correct way to write the number: (countrycode)(areacode)(phonenumber)
Example: +12125557777 (USA)
Example: +5511988887777 (BR)
    """)
    global var_key 
    var_key = str(input('Press ENTER to continue'))


def menu():
    while True:
        print(Fore.BLUE +
                """ 
   __        ___           _                                                 
   \ \      / / |__   __ _| |_ ___  __ _ _ __  _ __   
    \ \ /\ / /| '_ \ / _` | __/ __|/ _` | '_ \| '_ \   
     \ V  V / | | | | (_| | |_\__ \ (_| | |_) | |_) |    
      \_/\_/  |_| |_|\__,_|\__|___/\__,_| .__/| .__/    
                                        |_|   |_|       
 __  __                                  ____        _   
|  \/  | ___  ___ ___  __ _  __ _  ___  | __ )  ___ | |_ 
| |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \ |  _ \ / _ \| __|
| |  | |  __/\__ \__ \ (_| | (_| |  __/ | |_) | (_) | |_ 
|_|  |_|\___||___/___/\__,_|\__, |\___| |____/ \___/ \__|
                            |___/                         """)
        print('                                                      ')
        print('                                                      ')
        print(Fore.GREEN + 
              '    (1) Add numbers            |     (5) Send Message ')
        print('    (2) Show numbers           |     (6) Credits      ')
        print('    (3) Enter/Change Message   |     (7) Help         ')
        print('    (4) Show Message           |     (8) Leave        ')
        print('                                                      ')
        action = str(input(Fore.CYAN + '        Which action do you want to do: '))
        if action == '1':
            clear()
            add_numbers()
            clear()
        elif action == '2':
            clear()
            show_numbers()
            clear()
        elif action == '3':
            clear()
            write_message()
            clear()
        elif action == '4':
            clear()
            show_message()
            clear()
        elif action == '5':
            clear()
            send_message()
            clear()
        elif action == '6':
            clear()
            credits()
            clear()
        elif action == '7':
            clear()
            help()
            clear()
        elif action == '8':
            exit(1)
        else:
            print(Fore.RED + '\nMessage_bot Error: Invalid Action')



    

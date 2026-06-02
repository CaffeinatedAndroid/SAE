import Classes #MAIN FUNCTIONS STORED IN DEFS TO KEEP MENU SCRIPT CLEAN
import os


################################## MAIN MENU OPTIONS #########################################
def option_1():#View
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[32m _____________________________________________________\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                    ","\x1b[37m\x1b[1mTICKETS\x1b[0m","\x1b[32m                        |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")
    Classes.ShowAll()
    context_menu()

def option_2():#New
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[32m _____________________________________________________\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                    ","\x1b[37m\x1b[1mNEW TICKET\x1b[0m","\x1b[32m                     |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")
    Classes.AddNew()
    main_menu()

def option_3():#Information
    print("You selected Option 3.")
    info_menu()





################################ CONTEXT OPTIONS ###############################
def con_option_1():#Add
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[32m _____________________________________________________\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                    ","\x1b[37m\x1b[1mNEW TICKET\x1b[0m","\x1b[32m                     |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")
    Classes.AddNew()
    option_1()
    context_menu()

def con_option_2():#Select
    sel = input("Enter ticket ID: ")
    Classes.Select(sel)
    context_menu()
    return sel

def con_option_3():#Delete
    selected = input("Enter Ticket ID: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    Classes.Delete(selected)
    print("You selected Option 3.")
    context_menu()
    return selected

def con_option_4():#Filter
    sel = input("Enter Term: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    Classes.Filter(sel)
    context_menu()


################################ SUBCONTEXT OPTIONS ###############################
# def subCon_option_1():#Edit
#     #Classes.Edit(sel)
#     print("You selected Option 1.")
#     context_menu()

def subCon_option_2(selected):#Export
    selected = input("Enter Ticket ID: ")
    Classes.Export()
    context_menu()
    return selected

# def subCon_option_3():#Delete
#     Classes.Delete(sel)
#     print("You selected Option 3.")
#     context_menu()



############################### MENUS #######################################
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[32m _____________________________________________________\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                    ","\x1b[37m\x1b[1mTICKET MANAGER\x1b[0m","\x1b[32m                 |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")
    print("\x1b[32m| 1. View Tickets                           ___       |\x1b[0m")
    print("\x1b[32m| 2. New Ticket                            |[_]|      |\x1b[0m")
    print("\x1b[32m| 3. Information                           |+ ;|      |\x1b[0m")
    print("\x1b[32m| 0. Exit                                  `---'      |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")





    while True:
        choice = input("Enter your choice (0-3): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()

        elif choice == "0":
            print("Goodbye!")
            quit()
            break
        else:
            print("Invalid choice. Please try again.")


def context_menu():
    print("\x1b[32m|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\x1b[0m")
    print("\x1b[32m|   1.Add 2.Select 3.Delete 4.Filter 0.MainMenu       |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")

    while True:
        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            con_option_1()
        elif choice == "2":
            con_option_2()
        elif choice == "3":
            con_option_3()
        elif choice == "4":
            con_option_4()

        elif choice == "0":
            main_menu()
            break
        else:
            print("Invalid choice. Please try again.")

# def subContext_menu():
#     print("\x1b[32m|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\x1b[0m")
#     print("\x1b[32m|   1.Edit 2.Export 3.Delete 0.MainMenu               |\x1b[0m")
#     print("\x1b[32m|_____________________________________________________|\x1b[0m")
#
#     while True:
#         choice = input("Enter your choice (0-4): ")
#
#         # if choice == "1":
#         #     subCon_option_1()
#         if choice == "2":
#             subCon_option_2()
#         elif choice == "3":
#             subCon_option_3()
#
#         elif choice == "0":
#             main_menu()
#             break
#         else:
#             print("Invalid choice. Please try again.")

def info_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[32m _____________________________________________________\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                    ","\x1b[37m\x1b[1mTICKET MANAGER\x1b[0m","\x1b[32m                 |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                  Created by Todd C                  |\x1b[0m")
    print("\x1b[32m|          Now in ","\x1b[5m\x1b[31mc","\x1b[35mo","\x1b[32ml","\x1b[33mo","\x1b[36mr","\x1b[0m\x1b[32m for Rex :D              |\x1b[0m")
    print("\x1b[32m|        BEHOLD THE POWER OF ANSI ESCAPE CODES!!!     |\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|\x1b[34m ⠀⠀                 ⠀⠀⠀⣾⣽⣿⣿⡇⠀⠀⠀                      \x1b[32m|\x1b[0m")#Im doin a learnin
    print("\x1b[32m|\x1b[34m                  ⢀⠀⠀⠀⢀⣿⣿⠯⠍⠁ ⠀                       \x1b[32m|\x1b[0m")
    print("\x1b[32m|\x1b[34m                  ⢸⣦⣤⣾⣿⣿⣿⠓                           \x1b[32m|\x1b[0m")
    print("\x1b[32m|\x1b[34m                   ⠙⢿⣿⣿⡿⠃                            \x1b[32m|\x1b[0m")
    print("\x1b[32m|\x1b[34m          ⠀         ⠸⠏⠈⠇                             \x1b[32m|\x1b[0m")
    print("\x1b[32m|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\x1b[0m")
    print("\x1b[32m|   0.Main Menu                                       |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m")



    while True:
        choice = input("Enter your choice (0): ")
        if choice == "0":
            main_menu()
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()

"""
His palms are sweaty, knees weak, arms are heavy / There's errors on his terminal already, mom's spaghetti.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠴⠶⠶⠶⠤⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⣀⣤⠶⢶⡟⠋⠉⢹⠉⠉⠉⣟⠙⠓⢶⣤⡀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣴⠞⠋⣿⠀⠀⢸⠁⠀⣀⣼⣀⣀⣀⣟⠀⠀⢸⠈⠻⣦⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠋⡜⠀⠀⣿⣀⣤⡾⠿⣿⣏⡉⠉⠉⠉⠛⠻⠷⣾⡀⢸⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⣇⣠⣴⠿⠋⠁⡀⠀⠀⠉⠙⠂⠀⠀⠀⠀⠀⠈⠹⣿⡀⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣀⣴⣿⡟⠀⠀⠀⠀⠹⣿⠿⢶⡄⠀⠀⢀⡤⣞⣉⠉⠙⢻⡟⣻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠻⣿⠹⠤⠇⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⡖⢉⠙⢻⣿⣿⠆⣸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠟⠋⠙⢏⠉⠉⠓⠻⣧⣤⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⢸⠀⠀⠀⠀⠀⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣠⠞⠁⠀⠀⢄⠀⢣⠀⠀⢠⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⢰⣞⣉⣁⣨⡆⠀⠀⠀⣼⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠠⢄⡈⢷⡄⢧⣴⡟⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⠐⠛⠁⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠈⠛⢿⣏⣼⠁⠀⠀⢻⣆⠀⠀⠀⠀⠠⠖⠋⠛⢳⣤⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣀⠀⠀⠠⠤⠤⠤⣄⣘⣧⡀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠑⠶⠤⠤⠬⠑⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠉⠛⢶⣄⠀⠀⠀⠀⠀⠉⠙⣦⠀⠀⠀⠀⠙⢷⣄⡀⠀⢀⠀⠀⢀⣴⠟⠷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠉⠛⠳⢶⡶⠶⠟⠹⣧⠀⠈⠙⠓⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣦⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⢀⣠⣞⠁⠀⠀⠀⠘⣇⠀⠀⠀⠀⠘⣿⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠘⣧⠀⠀⠀⠀⠀⠈⠳⣤⡀⠀⠀⢹⠓⠦⣴⣒⠉⣉⣉⡛⠿⣶⣤⣄⡀⠸⡆⠀⠀⠀⠀⢹⡀⠙⣧⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠉⢶⡀⠀⢧⠀⠀⠈⠉⠉⠉⠉⠙⢮⢻⣦⠹⡄⢿⠀⠀⠀⠀⠈⣇⠀⠘⣧⠀⠀⠀⠀⠀⠀
⣿⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠘⣷⢤⣀⠀⠀⠀⠀⠀⠀⡇⢻⡇⢹⢼⡆⠀⠀⠀⠀⢹⡆⠀⢻⡀⣀⠀⠀⠀⠀
⣿⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠹⡄⠈⠓⠦⣄⠀⠀⣰⠇⣸⡇⢸⠎⣇⠀⠀⠀⠀⠈⣷⠀⠉⠙⢻⡀⠀⠀⠀
⣿⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢳⡀⠀⠀⠈⠙⠻⠭⣴⣿⣣⡞⠀⢻⠀⠀⠀⠀⠀⢸⡆⠀⢀⣿⣧⠀⠀⠀
⣿⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠸⡄⠀⠀⠀⠀⠀⣇⠀⢸⠀⠹⣧⠀⠀
⣿⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⣷⡀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠈⢳⡀
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠋⠁
#Thankyou for reading my skuffed spaghetti code - Todd.
"""

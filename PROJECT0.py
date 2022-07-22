import logging
import re
from PROJECT0MODULES import User

def main():


    while True:
        accountNo = input("\nEnter your account name: \n>>>")
        check = re.search(',', accountNo)
        try:
            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nNo commmas please\n")
            logging.error("Tried to enter a comma for name, trying again...")
        else:
            break


    while True:
        try:
            balance = float(input("\nEnter your balance credited by your former bank:\n>>>"))
        except ValueError as ve:
            print("\nError can only enter numbers please try again\n")
            logging.error("Tried to enter a string for balance, trying again...")
        else:
            break
    
    Choice_1 = 'r'
    print("\n Hello, Welcome to Fakebank! At any point you may select r to return to this menu:")
    print("\t1) Check account balance")
    print("\t2) No, Create an account")
    print("\t3 Request support")
    print("\t4) Deposit")
    print("\t5) Withdraw")
    if Choice_1 == "1":
        User.checkBalance
    if Choice_1 == "4":
        User.deposit
    if Choice_1 == "5":
        User.withdraw
            



# while True:   
#     try:
#             color = input("\nEnter animal's color:\n>>>")
#             check = re.search(',', color)

#             if check != None:
#                 raise ValueError
#         except ValueError as ve:
#             print("\nCANNOT HAVE COMMAS IN COLOR!\n")
#             logging.error("Tried to enter a comma for color, trying again...")
#         else:
#             break

if __name__ == "__main__":
    main()
from ast import In, IsNot
import random
from traceback import print_exc
import re
from Outlinemodules import Bank
def main():

    bank = Bank(firstName='', lastName='', accountNo=0, balance=0, pin=0)
    bank.welcome()
    fname = "Bankapp.csv"
    lst_bankData = []

    #add something in here to open Bankapp.csv
    #inside a while loop have a prompt for user to enter accountNo
    #have a loop
    for elem in lst_bankData:
        print(elem)
        print("\n\n") 

    while True:
        input_value = int(input('Enter 1 to enter account,\n2 to continue to the main menu where an account can be created\n'))


        if input_value == 1:
            bank.accountcheck()
            break
        else:
            break

    while True:
        input_value = int(input('Enter 1 to see your balance,\n2 to deposit\n3 to withdraw\n4 to create new account\n5 Log Out\n'))

        if input_value == 1:
            bank.checkBalance()
        elif input_value == 2:
            bank.deposit()
        elif input_value == 3:
            bank.withdraw()
        elif input_value == 4:
            bank.createAccounts()
        elif input_value == 5:
                bank.upload(fname)
                break
        elif input_value == 10:
            
                bank.displayList(fname)
        elif input_value=="quit":
            break

class Bank:
    def __init__(self, firstName, lastName, accountNo, balance, pin):
        self._firstName = str(firstName)
        self._lastName = str(lastName)
        self._accountNo = int(accountNo)
        self._balance = int(balance)
        self._pin = int(pin)
#creates accounts and gets multiple values used later on
    def createAccounts(self):

        self._accountNo = random.randint(100000000000, 999999999999)
        while (True):
            
            try:
                self._firstName = (input("Creating account... Please enter first name: "))
                self._firstName.split()
                c=0
                s='[@_!#$%^&*()<>?/\|}{~:]'
                for i in range(len(self._firstName)):
                    if self._firstName[i] in s:
                        c+=1
                    if c:
                        raise ValueError("No special characters!")
                    if any(i.isdigit() for i in self._firstName):
                        raise ValueError('Name must not contain any digits')
            except ValueError as e:
                print(e)
            except Exception as e:
                print_exc()
                print("Exception was raised... Trying again...")
            else:
                break
        while (True):
            try:
                self._lastName = str(input("Creating account... Please enter last name: "))
                self._lastName.split()
                c=0
                s='[@_!#$%^&*()<>?/\|}{~:]'
                for i in range(len(self._lastName)):
                    if self._lastName[i] in s:
                        c+=1
                    if c:
                        raise ValueError("No special characters!")
                    if any(i.isdigit() for i in self._lastName):
                        raise ValueError('Name must not contain any digits')
            except ValueError as e:
                print(e)
            except Exception as e:
                print_exc()
                print("Exception was raised... Trying again...")
            else:
                break
                
        while True:
            try:
                self._pin = (input("Enter your chosen pin "))
                num_format = re.compile(r'^\D{0}[0-9]{4}$\D{0}')
                it_is = re.match(num_format,self._pin)
                if it_is: 
                    print("Pin accepted")
                else: 
                    raise ValueError('Only numbers and only four digits please!')
            except ValueError as e:
                print(e)
            except Exception as e:
                print_exc()
                print("Exception was raised... Trying again...")
            else:
                break
        while (True):
            try:
                self._balance = (input("Enter the initial balance!"))
                num_format = re.compile(r'^\D{0}[0-9]$\D{0}')
                it_is = re.match(num_format,self._balance)
                if any(i.isdigit() for i in self._balance):
                    print('Correct')
                else:
                    raise ValueError("Only numbers please")
            except ValueError as e:
                print(e)
            except Exception as e:
                print_exc()
                print("Exception was raised... Trying again...")
            else:
                break
        print("You have entered " + self._firstName + " " + self._lastName +
              " and your account number is " + str(self._accountNo))
        print("Your current balance is " + str(self._balance))
        print("Your PIN is: " + str(self._pin))

        if int(self._balance) > 1:
            testing = (self._firstName,self._lastName, self._accountNo,self._balance,self._pin)
        else:
            testing=None
        
        return testing
#deposit method
    def deposit(self):
        if self._accountNo==0:
            print("Sorry you need to create an account first")
            return None

        while True:
            try:
                damount = int(float(input("Enter how much to deposit ")))
                if damount < 0:
                    raise ValueError("Must be positive number")
            except ValueError as ve:
                print(ve)
            except Exception as e:
                print_exc()
                print("Exception was raised... Trying again...")
            else:
                self._balance = int(self._balance) + damount
                self.checkBalance()
                break
#withdraw method
    def withdraw(self):
        if self._accountNo==0:
            print("Sorry you need to create an account first")
            return None

        while True:
            try:
                
                wamount = int(float(input("Enter how much to withdraw ")))
                if wamount > int(self._balance):
                    raise ValueError("Insufficent funds!")
                if wamount < 0:
                    raise ValueError("Must be positive number")
            except ValueError as ve:
                print(ve)
            except Exception as e:
                print_exc()
                print("Exception was raised... Trying again...")
            else:
                self._balance = int(self._balance) - wamount
                self.checkBalance()
                break
        #prints the current balance after usually a transaction
    def checkBalance(self):
        if self._accountNo==0:
            print("Sorry you need to create an account first")
            return None
        print("Your balance is " + str(self._balance))
    #Generic welcome
    def welcome(self):
        print("Welcome to andrew's fakebank!!!")
   #upload puts the data collected into the file Bankapp.csv 
    def upload(self,fname):
        if self._accountNo == 0:
            "No account created no output given thank you for using this bank!"
            return None
        fname = "Bankapp.csv"
        lst_bankData = []
        lst_bankData.append(self._firstName + "," + self._lastName + "," + str(self._accountNo) + "," + str(self._balance) + "," + str(self._pin))
        print(lst_bankData)
        with open("Bankapp.csv", "a+") as f:
            for bankData in lst_bankData:
                f.write(str(bankData) +"\n")
    def accountcheck(self):
        input_value = int(input('Enter account number\n'))
        lines_list = open('Bankapp.csv').read().splitlines()
        lst_bankData = []
        account_dict_list = lst_bankData
        for line in lines_list:
                    acc_dict = {}
                    acc_string_split = line.split(',')
                    acc_dict['first_name'] = acc_string_split[0]
                    acc_dict['last_name'] = acc_string_split[1]
                    acc_dict['account_number'] = acc_string_split[2]
                    acc_dict['balance'] = acc_string_split[3]
                    acc_dict['pin'] = acc_string_split[4]
                    account_dict_list.append(acc_dict)
        print(int(account_dict_list[0]["account_number"]))
        key,value = 'account_number',str(input_value)
        dictList = [ myDict for myDict in account_dict_list if myDict.get(key) == value ]
        print(dictList)
        if dictList[0]["account_number"] == str(input_value):
            print("true")
            self._firstName = dictList[0]['first_name']
            self._lastName = dictList[0]['last_name']
            self._accountNo = int(dictList[0]['account_number'])
            self._balance = int(float(dictList[0]['balance']))
            self._pin = int(dictList[0]['pin'])
            print("You have successfully logged in ")
            print(self._firstName)
            print(self._lastName)
            
        else:
            print("good try")
            print(dictList)
    def displayList(self,fname):
        
        lines_list = open(fname).read().splitlines()
        lst_bankData = []
        account_dict_list = lst_bankData
        for line in lines_list:
            check=False
            acc_dict = {}
            acc_string_split = line.split(',')
            for acc in account_dict_list:
                if acc['account_number'] == acc_string_split[2]:
                    acc['balance'] = acc_string_split[3]
                    check = True
                
            if check == False:
                acc_dict['first_name'] = acc_string_split[0]
                acc_dict['last_name'] = acc_string_split[1]
                acc_dict['account_number'] = acc_string_split[2]
                acc_dict['balance'] = acc_string_split[3]
                acc_dict['pin'] = acc_string_split[4]
                account_dict_list.append(acc_dict)
                print(acc_dict)  

def savedata(fname,lst_bankData,self):
        with open(fname, "w") as f:
            for testing in lst_bankData:
                if self._accountNo != 0:
                    f.write(testing._firstName + "," + (testing._lastName) + "," + str(testing._accountNo) + "," + str(testing._balance) + "," + str(testing._pin) + ",\n")
                else:
                    pass
def loaddata(fname)->list:
        lst_bankData = []

        with open(fname, "r") as f:
            for line in f:
                info = line.split(',')
                if info[2] != 0:
                    testing = (info[0], info[1], info[2], info[3], info[4])
                else:
                    testing = None

                if testing != None:
                    lst_bankData.append(testing)

        return lst_bankData











    #do a sort of check for accountNo = 0

if __name__ == "__main__":
    main()
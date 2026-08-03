class Bank_acc :
    def __init__(self, acc_id,name,current_bal ):
        self.id = acc_id
        self.name = name
        self.current_bal = current_bal

# function to deposit amount
    def amount_deposited (self,amount):
        self.current_bal += amount
        print(f"{amount:.2f} has been deposited to your account")
        self.my_balance()
# function to withdraw amount         
    def amount_withdrawal(self,amount):
        if self.current_bal >= amount:
            self.current_bal -= amount
            print(f"{amount: .2f}  has been withdrawed from your account")
        else:
            print("Insufficient Balance")
        self.my_balance()
#function to check balance        
    def my_balance (self):
        print(f" Your total Balance : {self.current_bal: .2f}") 
#function to show info
    def show_info (self):
        print(f"Your Account ID is :{self.id}\nYour name is : {self.name}\nYour Current Balance is {self.current_bal:.2f}")

        
#code that will only execute in this file
if __name__ == "__main__":
#empty dictionary to store my bank acccounts with id
    accounts= {}        
    id_index = 1
    while True:

        print("/nWelcome to the Bank.")
        print("1)Create an account .")
        print("2)Acess your account.")
        print("3)Exit Bank_acc.")
        Choice = int(input("Select a Option 1/2/3. :"))
        if Choice == 1:

            bal=float(input("enter your balance :"))
            name = input("enter your name :")
            account = Bank_acc(id_index,name,bal)
            
            accounts[id_index] = account 
            print(f"Your account has been created.\nYour id is {id_index}")
            id_index += 1
        elif Choice == 2 :
            acc_id = int(input("enter your ID :"))
            if acc_id not in accounts:
                print("Account donot exist.")    
                continue
            account = accounts[acc_id]
            account.show_info()
            while True:
                print(f"\n what do you want?")
                print(f"a. withdraw")
                print(f"b. deposit")
                print(f"c.know your balance")
                print(f"d. exit to main menu")
                user_choice = input("enter your choice a/b/c/d :").lower()
                if user_choice == "a" :
                    amount = float(input("enter amount to withdraw :"))
                    account.amount_withdrawal(amount)
                elif user_choice == "b" :                    
                    amount = float(input("enter amount to deposit :"))        
                    account.amount_deposited(amount)
                elif user_choice == "c" :
                    account.my_balance()
                elif user_choice == "d" :
                    print("Back to the main menu..")
                    break
                else:
                    print("enter a valid input")
        elif Choice == 3 :
            print ("Thanks for coming...\n Bye...")
            break
        else:
            print("enter a valid choice.")                    
                  


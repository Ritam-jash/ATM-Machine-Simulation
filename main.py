class ATM:  
    def __init__(self, account_balance=0, pin="1234"):  
        self.account_balance = account_balance  
        self.pin = pin  
        self.transaction_history = []  

    def display_balance(self):  
        print(f"Account Balance: {self.account_balance}")  
    
    def deposit(self, amount):  
        if amount > 0:  
            self.account_balance += amount  
            self.transaction_history.append(f"Deposited: {amount}")  
            print(f"{amount} deposited successfully.")  
        else:  
            print("Deposit amount must be positive.")  

    def withdraw(self, amount):  
        if amount > 0:  
            if amount <= self.account_balance:  
                self.account_balance -= amount  
                self.transaction_history.append(f"Withdrawn: {amount}")  
                print(f"{amount} withdrawn successfully.")  
            else:  
                print("Insufficient funds.")  
        else:  
            print("Withdrawal amount must be positive.")  
    
    def change_pin(self, new_pin):  
        if new_pin.isdigit() and len(new_pin) == 4:  
            self.pin = new_pin  
            print("PIN changed successfully.")  
        else:  
            print("New PIN must be a 4-digit number.")  
    
    def view_transaction_history(self):  
        if self.transaction_history:  
            print("Transaction History:")  
            for transaction in self.transaction_history:  
                print(transaction)  
        else:  
            print("No transactions yet.")  

def main():  
    atm = ATM()  
    
    while True:  
        print("\nWelcome to the ATM\nPlease insert your card")
        password = input("Please enter your PIN: ")

        if password == atm.pin:
            print("1. Check Balance")  
            print("2. Deposit Money")  
            print("3. Withdraw Money")  
            print("4. Change PIN")  
            print("5. View Transaction History")  
            print("6. Exit")  

            choice = input("Choose an option: ")  

            if choice == '1':  
                atm.display_balance()  
            elif choice == '2':  
                amount = float(input("Enter amount to deposit: "))  
                atm.deposit(amount)  
            elif choice == '3':  
                amount = float(input("Enter amount to withdraw: "))  
                atm.withdraw(amount)  
            elif choice == '4':  
                new_pin = input("Enter new 4-digit PIN: ")  
                atm.change_pin(new_pin)  
            elif choice == '5':  
                atm.view_transaction_history()  
            elif choice == '6':  
                print("Thank you for using the ATM!")  
                break  
            else:  
                print("Invalid choice. Please try again.")
        else:
            print("Wrong PIN, please try again.")

if __name__ == "__main__":  
    main()  

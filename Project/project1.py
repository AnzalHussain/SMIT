import os

class BankAccount:
    def __init__(self, name, initial_balance=0.0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []
        self.file_name = f"{self.name}_transactions.txt"
        if os.path.exists(self.file_name):
            self._load_transactions()
            print(f"Welcome back, {self.name}. Your current balance is {self.balance}.")
        else:
            print(f"Account created for {self.name} with initial balance {self.balance}.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return

        self.balance += amount
        transaction = f"Deposit: {amount}. New Balance: {self.balance}"
        self.transactions.append(transaction)
        self._log_transaction(transaction)
        print(transaction)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        transaction = f"Withdrawal: {amount}. New Balance: {self.balance}"
        self.transactions.append(transaction)
        self._log_transaction(transaction)
        print(transaction)

    def check_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance

    def print_statement(self):
        print(f"Account statement for {self.name}:")
        for transaction in self.transactions:
            print(transaction)

    def _log_transaction(self, transaction):
        with open(self.file_name, "a") as file:
            file.write(transaction + "\n")

    def _load_transactions(self):
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                transaction = line.strip()
                self.transactions.append(transaction)
                if transaction.startswith("Deposit"):
                    amount = float(transaction.split()[1].strip(".:"))
                    self.balance += amount
                elif transaction.startswith("Withdrawal"):
                    amount = float(transaction.split()[1].strip(".:"))
                    self.balance -= amount

# Menu-driven interface

def main():
    name = input("Enter account holder's name: ")
    account = BankAccount(name)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.print_statement()
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

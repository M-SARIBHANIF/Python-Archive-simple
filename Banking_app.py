import time
import threading
import random

# Defining a class bank account
class Bank:
    def __init__(self,Id, initial_balance):
        self.account_id = Id
        self.balance = initial_balance
        # Create a lock for thread safety
        self.lock = threading.Lock()
    def deposit_ammount(self, amount):
        #locking before depositing
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_id}")
            print(f"New balance: {self.balance}")
    def withdraw_ammount(self, amount):
        #locking before withdrawing
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_id}")
                print(f"New balance: {self.balance}")
            else:
                print(f"Insufficient balance in account {self.account_id}")
    def check_balance(self):
        # locking before checking balance
        with self.lock:
            print(f"Account {self.account_id} balance: {self.balance}")

# Function to simulate bank operations on an account
def Bank_working(account, no_operations):
    for items in range(no_operations):
        operation = random.choice(["1.deposit", "2.withdraw", "3.check_balance"])
        if operation == "1.deposit":
            amount = random.randint(100, 1000)
            account.deposit_ammount(amount)
        elif operation == "2.withdraw":
            amount = random.randint(50, 500)
            account.withdraw_ammount(amount)
        elif operation == "3.check_balance":
            account.check_balance()
        time.sleep(1)

if __name__ == "__main__":
    no_of_accounts = 2
    num_threads_per_account = 1
    no_of_operations = 4
    # Create a list of bank accounts with starting balances
    accounts = [Bank(account_id, 450) for account_id in range(no_of_accounts)]
    Threads = []

    # Create threads to simulate bank operations for each account
    for account in accounts:
        for item in range(num_threads_per_account):
            thread = threading.Thread(target=Bank_working, args=(account, no_of_operations))
            Threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in Threads:
        thread.join()

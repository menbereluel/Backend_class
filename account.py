from datetime import datetime
class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type 

    def __str__(self):
        sign = '+' if self.transaction_type in ['deposit', 'loan', 'interest'] else '-'
        return f"{self.date_time} | {self.transaction_type.title()} | {self.narration} | {sign}{self.amount}"

class Account:
    def __init__(self, name,account_number):
        self.name = name
        self._account_number=account_number
        self._transactions=[]
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.frozen = False
        self.min_balance = 0
        self.closed = False

    def deposit(self, amount):
        if self.closed:
            return "Account is closed."
        if self.frozen:
            return "Account is frozen. Cannot deposit."
        if amount <= 0:
            return "Deposit must be a positive amount."
        self._transactions.append(Transaction("Deposit", amount, "deposit"))
        return f"Confirmed, you have received {amount}. New balance is {self.get_balance()}"


    def withdraw(self, amount):
        if self.closed:
            return "Account is closed."
        if self.frozen:
            return "Account is frozen. Cannot withdraw."
        if amount <= 0:
            return "Withdraw amount must be positive."
        if self.get_balance() - amount < self.min_balance:
            return "Insufficient funds or below minimum balance requirement."
        self._transactions.append(Transaction("Withdrawal", amount, "withdrawal"))
        return f"Confirmed, you have withdrawn {amount}. New balance is {self.get_balance()}"

    def transfer(self, amount, recipient_account):
        if self.closed:
            return "Account is closed."
        if self.frozen:
            return "Account is frozen. Cannot transfer."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.get_balance() - amount < self.min_balance:
            return "Insufficient funds or below minimum balance requirement."
        self._transactions.append(Transaction(f"Transfer to {recipient_account.name}", amount, "withdrawal"))
        recipient_account.receive_transfer(amount, self.name)
        return f"Transferred {amount} to {recipient_account.name}. New balance is {self.get_balance()}"

    def receive_transfer(self, amount, sender_name):
        self._transactions.append(Transaction(f"Transfer from {sender_name}", amount, "deposit"))

    def get_balance(self):
        balance = 0
        for t in self._transactions:
            if t.transaction_type in ['deposit', 'loan', 'interest']:
                balance += t.amount
            elif t.transaction_type == 'withdrawal':
                balance -= t.amount
        return balance

    def request_loan(self, amount):
        if self.closed:
            return "Account is closed."
        if amount <= 0:
            return "Loan amount must be positive."
        self.loan += amount
        self._transactions.append(Transaction("Loan granted", amount, "loan"))
        return f"Loan of {amount} approved. New balance is {self.get_balance()}"


    def repay_loan(self, amount):
        if self.closed:
            return "Account is closed."
        if amount <= 0:
            return "Repayment must be a positive amount."
        if amount > self.get_balance():
            return "Insufficient balance to repay loan."
        self._transactions.append(Transaction("Loan repayment", amount, "withdrawal"))
        self.loan -= amount
        if self.loan < 0:
            self.loan = 0
        return f"Loan repayment of {amount} successful. Remaining loan balance is {self.loan}"

    def view_account_details(self):
         return f"Account Owner: {self.name}, Account Number: {self._account_number}, Balance: {self.get_balance()}, Loan Balance: {self.loan}"
      
    def change_owner(self, new_name):
        if self.closed:
            return "Account is closed."
        self.name = new_name
        return f"Account owner updated to {self.name}"

    def account_statement(self):
        print("---- Account Statement ----")
        for t in self._transactions:
            print(t)
        print(f"Current Balance: {self.get_balance()}")
        print(f"Outstanding Loan: {self.loan}")


    def apply_interest(self):
        if self.closed:
            return "Account is closed."
        interest = self.get_balance() * 0.05
        self._transactions.append(Transaction("Interest applied", interest, "interest"))
        return f"Interest of {interest} applied. New balance is {self.get_balance()}"

    def freeze_account(self):
        self.frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance must be non-negative."
        self.min_balance = amount
        return f"Minimum balance set to {self.min_balance}"

    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan = 0
        self.closed = True
        return "Account has been closed. All balances cleared."
account_menbere=Account("Menbere",10000327367)
print(account_menbere.deposit(200000))
print(account_menbere.withdraw(6000))
print(account_menbere.account_statement())

        
 
      


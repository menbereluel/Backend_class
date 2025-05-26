class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
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
        self.deposits.append(amount)
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
        self.withdrawals.append(amount)
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
        self.withdrawals.append(amount)
        recipient_account.deposit(amount)
        return f"Transferred {amount} to {recipient_account.name}. New balance is {self.get_balance()}"

    def get_balance(self):
        return sum(self.deposits) - sum(self.withdrawals)

    def request_loan(self, amount):
        if self.closed:
            return "Account is closed."
        if amount <= 0:
            return "Loan amount must be positive."
        self.loan += amount
        self.deposits.append(amount)
        return f"Loan of {amount} approved. New balance is {self.get_balance()}"

    def repay_loan(self, amount):
        if self.closed:
            return "Account is closed."
        if amount <= 0:
            return "Repayment must be a positive amount."
        if amount > self.get_balance():
            return "Insufficient balance to repay loan."
        self.withdrawals.append(amount)
        self.loan -= amount
        if self.loan < 0:
            self.loan = 0
        return f"Loan repayment of {amount} successful. Remaining loan balance is {self.loan}"

    def view_account_details(self):
        return f"Account Owner: {self.name}, Balance: {self.get_balance()}, Loan Balance: {self.loan}"

    def change_owner(self, new_name):
        if self.closed:
            return "Account is closed."
        self.name = new_name
        return f"Account owner updated to {self.name}"

    def account_statement(self):
        print("---- Account Statement ----")
        for i, amount in enumerate(self.deposits):
            print(f"Deposit {i+1}: +{amount}")
        for i, amount in enumerate(self.withdrawals):
            print(f"Withdrawal {i+1}: -{amount}")
        print(f"Current Balance: {self.get_balance()}")
        print(f"Outstanding Loan: {self.loan}")

    def apply_interest(self):
        if self.closed:
            return "Account is closed."
        interest = self.get_balance() * 0.05
        self.deposits.append(interest)
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

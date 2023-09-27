from abc import ABCMeta, abstractmethod

"""
Practice example: Design a bank application that allows users to deposit and withdraw money from their accounts.
"""


class Overdrawn(Exception):
    pass


class FailedTransferDueToOverdrawn(Exception):
    pass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def print(self):
        pass


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance is {self.balance}.")
        else:
            raise Overdrawn("You cannot withdraw more than your balance.")


class DepositCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)

    def undo(self):
        self.account.withdraw(self.amount)

    def print(self):
        print(f"Deposit: {self.amount}")


class WithdrawCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount)

    def undo(self):
        self.account.deposit(self.amount)

    def print(self):
        print(f"Withdraw: {self.amount}")


class Transfer(Command):
    def __init__(self, account_from, account_to, amount):
        self.account_from = account_from
        self.account_to = account_to
        self.amount = amount

    def print(self):
        print(f"Transfer: from {self.account_from} to {self.account_to}")

    def execute(self):
        try:
            WithdrawCommand(self.account_from, self.amount).execute()
        except Overdrawn:
            raise FailedTransferDueToOverdrawn(
                "You cannot transfer more than your balance."
            )
        DepositCommand(self.account_to, self.amount).execute()

    def undo(self):
        WithdrawCommand(self.account_to, self.amount).execute()
        DepositCommand(self.account_from, self.amount).execute()


class AccountingBook:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)
        command.execute()

    def undo_all(self):
        for command in reversed(self.commands):
            command.undo()

    def undo_last(self):
        last_command = self.commands.pop()
        last_command.undo()

    def print_history(self):
        for command in self.commands:
            command.print()


toms_account = Account(100)
bills_account = Account(0)


book = AccountingBook()
book.add_command(DepositCommand(bills_account, 100))
book.add_command(WithdrawCommand(toms_account, 100))
book.add_command = Transfer(toms_account, bills_account, 50)

print("\n\nHistory:\n")
book.print_history()
book.undo_last()
book.print_history()


"""
As commands are added, they are automitically executed

"""

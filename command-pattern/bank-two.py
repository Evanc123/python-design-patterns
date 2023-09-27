from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def undo(self):
        ...

    @abstractmethod
    def pprint(self):
        ...


class OverdrawnException(Exception):
    ...


class Account:
    def __init__(self, name: str, initial_amount=0):
        self.name = name
        self.fund_amount = initial_amount

    def add_funds(self, amount_to_add: float):
        self.fund_amount += amount_to_add

    def withdraw_funds(self, amount_to_withdraw: float):
        if self.fund_amount - amount_to_withdraw >= 0:
            self.fund_amount -= amount_to_withdraw
        else:
            raise OverdrawnException


class Deposit(Command):
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.add_funds(amount_to_add=self.amount)

    def undo(self):
        self.account.withdraw_funds(amount_to_withdraw=self.amount)

    def pprint(self):
        print(f"Deposit {self.amount} into Account {self.account.name}")


class Withdraw(Command):
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount
        self.caused_overdraw = False

    def execute(self):
        try:
            self.account.withdraw_funds(amount_to_withdraw=self.amount)
        except OverdrawnException:
            self.caused_overdraw = True

    def undo(self):
        if not self.caused_overdraw:
            self.account.add_funds(amount_to_add=self.amount)

    def construct_overdrawn_string(self):
        return "Note: Caused Overdraw, skipped" if self.caused_overdraw else ""

    def pprint(self):
        print(
            f"Withdraw {self.amount} from Account {self.account.name} {self.construct_overdrawn_string()}"
        )


class Transfer(Command):
    def __init__(self, from_account: Account, to_account: Account, amount: float):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.is_rollback = False

    def execute(self):
        withdraw = Withdraw(self.from_account, self.amount)
        withdraw.execute()
        if withdraw.caused_overdraw:
            self.is_rollback = True
        else:
            Deposit(self.to_account, self.amount).execute()

    def undo(self):
        if self.is_rollback:
            pass
        else:
            Withdraw(self.to_account, self.amount).execute()
            Deposit(self.from_account, self.amount).execute()

    def construct_rollback_string(self):
        return "Note: Caused Rollback, skipped" if self.is_rollback else ""

    def pprint(self):
        print(
            f"Transfer {self.amount} from {self.from_account.name} to {self.to_account.name} {self.construct_rollback_string()}"
        )


class AccountingBook:
    def __init__(self):
        self.history: List[Command] = []

    def add_command(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        last_command = self.history.pop(-1)
        last_command.undo()

        print("Undoing:")
        last_command.pprint()

    def print_book(self):
        for command in self.history:
            command.pprint()


bobs_account = Account("bob", 100)
alices_account = Account("alice", 50)

accounting_book = AccountingBook()

accounting_book.add_command(Withdraw(bobs_account, 100))
accounting_book.add_command(Deposit(alices_account, 100))
accounting_book.add_command(Withdraw(bobs_account, 100))
accounting_book.add_command(Withdraw(bobs_account, 100))
accounting_book.undo_last()
accounting_book.undo_last()
accounting_book.undo_last()
accounting_book.add_command(Transfer(alices_account, bobs_account, 200))
accounting_book.add_command(Transfer(alices_account, bobs_account, 50))
accounting_book.undo_last()


accounting_book.print_book()


print("\n\n")
print(f"Bob Total: {bobs_account.fund_amount}")
print(f"Alice Total: {alices_account.fund_amount}")

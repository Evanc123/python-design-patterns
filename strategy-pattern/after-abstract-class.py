# taken from https://github.com/ArjanCodes/betterpython/blob/main/3%20-%20strategy%20pattern/strategy-before.py

import string
import random
from typing import List
from abc import ABC, abstractmethod


class SupportTicket:
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class OrderingStrategy(ABC):
    @abstractmethod
    def order_tickets(self, tickets: List[SupportTicket]):
        pass


class FIFO(OrderingStrategy):
    def order_tickets(self, tickets: List[SupportTicket]):
        return tickets


class FILO(OrderingStrategy):
    def order_tickets(self, tickets: List[SupportTicket]):
        list_copy = tickets.copy()
        return list_copy.reverse()


class Random(OrderingStrategy):
    def order_tickets(self, tickets: List[SupportTicket]):
        list_copy = tickets.copy()
        random.shuffle(list_copy)
        return list_copy


def generate_id(length=8):
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class CustomerSupport:
    def __init__(self, ticket_orderer: OrderingStrategy):
        self.tickets = []
        self.ticket_orderer = ticket_orderer

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        self.tickets = self.ticket_orderer.order_tickets(self.tickets)
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in self.tickets:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport(ticket_orderer=Random())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()

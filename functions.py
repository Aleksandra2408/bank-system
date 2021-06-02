import random
import sqlite3


class Account:

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def output(self, transfer):
        self.balance = self.balance - transfer

    def income(self, transfer):
        self.balance = self.balance + transfer

    def insert(self, conn):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO card (number, pin, balance) VALUES (' + str(self.card_number) + ', ' + str(self.pin) + ', ' + str(self.balance) + ')')
        conn.commit()

    def update(self, conn):
        cursor = conn.cursor()
        cursor.execute('UPDATE card SET balance = ' + str(self.balance) + ' WHERE number =' + str(self.card_number))
        conn.commit()

    def data_check(self, card_number, pin):
        if self.card_number == card_number and self.pin == pin:
            return True
        else:
            return False

    def print(self, print_balance = False):
        print('')
        print('Your card number:')
        print(self.card_number)
        print('Your card PIN:')
        print(self.pin)
        if print_balance:
            print('Your balance:')
            print(self.balance)
        print('')


# after all tasks: insert or update, print

# create first account
fa = Account(123456, 9876)

# create second account
sa = Account(654321, 1234)

# income to fa 1000
fa.income(1000)
fa.print(True)

# transfer from fa to sa 500

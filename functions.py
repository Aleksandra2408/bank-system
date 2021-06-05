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

    def delete(self, card_number, conn):
        if self.card_number == card_number:
            del self
        cursor.execute('DELETE FROM card WHERE number =' + str(self.card_number))
        conn.commit()

    def print(self, print_balance=False):
        print('')
        print('Your card number:')
        print(self.card_number)
        print('Your card PIN:')
        print(self.pin)
        if print_balance:
            print('Your balance:')
            print(self.balance)
        print('')




def create_card_number():
    card_number = list('400000' + str(int(random.randint(100000000, 999999999))))
    c = list.copy(card_number)
    for i in range(len(c)):
        old_value = c[i]
        new_value = int(old_value)
        c[i] = new_value
    for index, i in enumerate(c):
        if index % 2 == 0:
            i = i * 2
        c[index] = i
        if c[index] > 9:
            c[index] = c[index] - 9
    a = 0
    if sum(c) % 10 > 0:
        a = abs(10 - (sum(c) % 10))
    card_number.append(a)
    card_number = int("".join(map(str, card_number)))
    return card_number


# after all tasks: insert or update, print

# create first account
fa = Account(123456, 9876)
fa.card_number = create_card_number()

# create second account
sa = Account(654321, 1234)
sa.card_number = create_card_number()

# income to fa 1000
fa.income(1000)
fa.print(True)

# transfer from fa to sa 500
fa.output(500)
sa.income(500)
fa.print(True)
sa.print(True)

# основной код
conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()

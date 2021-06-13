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

    def insert(self, conn, card_number):
        cursor.execute('UPDATE card SET balance = ' + str(self.balance) + ' WHERE number =' + str(card_number))
        conn.commit()

    def data_check(self, card_number, pin):
        if self.card_number == card_number and self.pin == pin:
            return True
        else:
            return False

    def delete(self, card_number, conn):
        cursor.execute('DELETE FROM card WHERE number =' + str(self.card_number))
        conn.commit()
        if self.card_number == card_number:
            del self

    def income_transfer(self, card_number, transfer_funds):
        if self.card_number == card_number:
            self.balance = self.balance + transfer_funds

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


def welcome():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    answer = int(input())
    return answer


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


def account_menu():
    print('')
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')
    selected_item = int(input())
    return selected_item


def create_account(conn, cursor):
    card_number = create_card_number()
    pin = random.randint(1111, 9999)
    account = Account(card_number, pin)
    all_accounts.append(account)
    insert = 'INSERT INTO card (number, pin, balance) VALUES (' + str(account.card_number) + ', ' + str(account.pin) + ', ' + str(account.balance) + ');'
    cursor.execute(insert)
    conn.commit()
    print(all_accounts)
    return account


def luhn_chek(num_for_transf):
    card_number = list(str(num_for_transf))
    copy_card_number = list.copy(card_number)
    for i in range(len(copy_card_number)):
        old_value = copy_card_number[i]
        new_value = int(old_value)
        copy_card_number[i] = new_value
    for index, i in enumerate(copy_card_number):
        if index % 2 == 0:
            i = i * 2
        copy_card_number[index] = i
        if copy_card_number[index] > 9:
            copy_card_number[index] = copy_card_number[index] - 9
    if sum(copy_card_number) % 10 > 0:
        return False
    else:
        return True


def transfer_money(card_number, account):
    num_for_transf = int(input())
    if num_for_transf == card_number:
        print("You can't transfer money to the same account!")
    elif luhn_chek(num_for_transf) is False:
        print('Probably you made a mistake in the card number. Please try again!')
    elif luhn_chek(num_for_transf) is True:
        cursor.execute('SELECT id FROM card WHERE number = ' + str(num_for_transf))
        id_exists = cursor.fetchall()
        if len(id_exists) == 0:
            print(id_exists)
            print('Such a card does not exist.')
        else:
            print(id_exists)
            print(id_exists[0][0])
            print('Enter how much money you want to transfer:')
            transfer_funds = int(input())
            if transfer_funds > account.balance:
                print('Not enough money!')
            else:
                account.output(transfer_funds)
                account.insert(conn, card_number)
                for account in all_accounts:
                    if account.card_number == num_for_transf:
                        account.income_transfer(num_for_transf, transfer_funds)
                        account.insert(conn, num_for_transf)

conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()
cursor.execute('DROP TABLE card')
cursor.execute('CREATE TABLE card ( id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

all_accounts = []
answer = welcome()

while answer != 0:
    if answer == 1:
        account = create_account(conn, cursor)
        account.print()
        answer = welcome()
    elif answer == 2:
        print('Enter your card number:')
        card_number = int(input())
        print('Enter your PIN:')
        pin = int(input())
        print('')
        for account in all_accounts:
            if account.card_number == card_number:
                if account.data_check(card_number, pin) is True:
                    print('You have successfully logged in!')
                    selected_item = account_menu()
                    while selected_item != 0:
                        if selected_item == 1:
                            print(account.balance)
                            selected_item = account_menu()
                        elif selected_item == 2:
                            print("Enter income:")
                            income = int(input())
                            account.income(income)
                            account.insert(conn, card_number)
                            selected_item = account_menu()
                        elif selected_item == 3:
                            print('Transfer')
                            print('Enter card number:')
                            transfer_money(card_number, account)
                            selected_item = account_menu()
                        elif selected_item == 4:
                            account.delete(card_number, conn)
                            print('The account has been closed!')
                            print('')
                            selected_item = 'wrong'
                            answer = welcome()
                            break
                        elif selected_item == 5:
                            print('You have successfully logged out!')
                            print('')
                            selected_item = 'wrong'
                            answer = welcome()
                            break
                    else:
                        answer = 0
                        break
                else:
                    print('Wrong card number or PIN!')
                    print('')
                    answer = welcome()
            else:
                print('Wrong card number or PIN!')
                print('')
                answer = welcome()
print('Bye!')

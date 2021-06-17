# Simple Banking System

#### About

Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. In this project, you will develop a simple banking system with database.

#### Learning outcomes
In this project, you will find out how the banking system works and learn about SQL. We'll also see how Luhn algorithm can help us avoid mistakes when entering the card number. As an overall result, you'll get new experience in Python.

## Stage 1/4: Card anatomy

 **Topics learned:**

> Computer programming
> 
> Introduction to OOP
> 
> Introduction to Python
> 
> Overview of the basic program
>
> PEP 8
>
> Comments
>
> Basic data types
>
> Integer arithmetic
> 
> Quotes and multi-line strings
>
> Variables
>
> Type casting
>
> Naming variables
> 
> Taking input
>
> String formatting
>
> Program with numbers
> 
> Boolean logic
>
> Comparisons
>
> Dictionary
>
>Invoking a function
>
> Declaring a function
>
> Scopes
> If statement
>
> Else statement
>
> Elif statement
>
> While loop
>
> For loop
>
> Loop control statements
>
> Load module
>
> Random module
>
> Class
>
> Class instances
>
> Methods
> 
> Methods and attributes

###### Objectives

You should allow customers to create a new account in our banking system.
Once the program starts, you should print the menu:
```
1. Create an account
2. Log into account
0. Exit

```

If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. A PIN code is a sequence of any 4 digits. PIN should be generated in a range from 0000 to 9999.
If the customer chooses ‘Log into account’, you should ask them to enter their card information. Your program should store all generated data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin. You can use an array to store the information.
After all information is entered correctly, you should allow the user to check the account balance; right after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

## Stage 2/4: Luhn algorithm

###### Objectives
You should allow customers to create a new account in our banking system.
Once the program starts you should print the menu:
```
1. Create an account
2. Log into the account
3. Exit
```

If the customer chooses ```Create an account’```, you should generate a new card number that satisfies all the conditions described above.

Then you should generate a PIN code that belongs to the generated card number. PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.

If the customer chooses ```Log into account```, you should ask to enter card information.

After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.


## Stage 3/4: I'm so lite

 **Topics learned:**

> Introduction to operating systems
>
> Files
>
> Introduction to databases
>
> What is SQL
>
> Basic data types
>
> Literals
>
> Expressions
>
> Basic SELECT statement
> 
> SELECT FROM statement
>
> SELECT FROM WHERE statement
>
> Basic CREATE statement
>
> Basic INSERT statement

###### Objectives

In this stage, create a database named ```card.s3db``` with a table titled ```card```. It should have the following columns:
* id INTEGER
* number TEXT
* pin TEXT
* balance INTEGER DEFAULT 0

Pay attention: your database file should be created when the program starts if it hasn’t yet been created. And all created cards should be stored in the database from now.

# Stage 4/4: Advanced system

 **Topics learned:**

> Basic DELETE statement

###### Objectives

You have created the foundation of our banking system. Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.
Now your menu should look like this:
```
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
```
If the user asks for ```Balance```, you should read the balance of the account from the database and output it into the console.
```Add income``` item should allow us to deposit money to the account.
```Do transfer``` item should allow transferring money to another account. You should handle the following errors:
* If the user tries to transfer more money than he/she has, output: ```Not enough money!```
* If the user tries to transfer money to the same account, output the following message: ```You can't transfer money to the same account!```
* If the receiver's card number doesn’t pass the Luhn algorithm, you should output: ```Probably you made a mistake in the card number. Please try again!```
* If the receiver's card number doesn’t exist, you should output: ```Such a card does not exist.```
* If there is no error, ask the user how much money they want to transfer and make the transaction.
If the user chooses the ```Close account``` item, you should delete that account from the database.






"""
main programe of bank.py,
first thing need to do is importing the bank.py



"""

from bank  import *

the_bank = Bank()#create the bank
user_anna = User("anna", "my_password")#create the user

#the_bank.add_user(user_anna)# add the user_anna to the bank

print "Main program created the user " + user_anna.username




is_logged_in = the_bank.login(user_anna.username, user_anna.password)

if is_logged_in:#after login, the bank provide service to the user
    print
    print "*"*20
    print "Login Successful"
    print "*"*20
    print

    account_anna = Account(user_anna)
    account_anna.deposite_money(100)

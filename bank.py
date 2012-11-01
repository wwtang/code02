class Bank:

    def __init__(self):
        self.usernamePasswordsDictionary = {}
        self.users = []

    def add_user(self, username, password):
    #def add_user(self, user):
        
        user = User(username, password)
        
        self.usernamePasswordsDictionary[user.username] = user.password

        self.users.append(user)
        
        print "Bank add user: %s to the bank" %user.username
        return user

    def add_account(self, user):
        account = Account(user)
        print "Bank added account " + account.user.username + "with %d bucks" % account.balance
        
    def login(self, username, password):
        if self.usernamePasswordsDictionary[username] == password:
            return True
        print "The User: %s is not exist in the Bank"% username
        return False

    def transfer_money(self, amount, uesr_from, user_to):
        if user_from.account.withdraw_money(amount):
            user_to.account.deposite_money(amount)

    def print_account(self):
        for u in self.users:
            print "%s has %d in their account" %(u.user.name, u.account.balance )
            
    def detail(self):
        print "user list: "
        print [user for user in self.usernamePasswordsDictionary]


class User:
    """ name, original balance"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def detail(self):
        print "Username:  %s. Password: ********" % self.username


class Account:
    def __init__(self, user):
        self.user = user
        self.balance = 0#default balance is 0 buck

    def deposite_money(self, amount):
        self.balance = self.balance + amount
        print "Account just added %d bucks. And current balance is : %s " % (amount, self.balance)


    def withdraw_money(self, amount):
        if self.balance > amount:
            
            self.balance = self.balance - amount
            print "Account just withdrew %d bucks. And the current balance is: %s" %( amount, self.balance)
            return True
        else:
            print "Withdraw Aborted: You don't have enough money in your account"
            return False





        

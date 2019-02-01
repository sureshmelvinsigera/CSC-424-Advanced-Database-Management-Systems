class Account(object):
    """
    A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance):
        """Return a Customer object whose name is *name*.
        :param name:
        :param balance:
        """
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars.
        :param amount:
        :return:
        """
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars.
        :param amount:
        :return:
            balance
        """
        self.balance += amount
        return self.balance

    def print_info(self):
        """Prints account information
        :return:
            None
        """
        print('-----------------------------')
        print('Customer name : ', self.name)
        print('Balance : $', self.balance)
        print('-----------------------------\n')

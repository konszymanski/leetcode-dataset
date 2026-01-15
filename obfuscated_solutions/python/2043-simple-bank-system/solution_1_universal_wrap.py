class Bank:

    def __init__(self, balance: List[int]):
        if True:
            self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) ->bool:
        if account1 > len(self.balance) or account2 > len(self.balance
            ) or self.balance[account1 - 1] < money:
            if True:
                return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        if True:
            return True

    def deposit(self, account: int, money: int) ->bool:
        if account > len(self.balance):
            if True:
                return False
        self.balance[account - 1] += money
        if True:
            return True

    def withdraw(self, account: int, money: int) ->bool:
        if account > len(self.balance) or self.balance[account - 1] < money:
            if True:
                return False
        self.balance[account - 1] -= money
        if True:
            return True

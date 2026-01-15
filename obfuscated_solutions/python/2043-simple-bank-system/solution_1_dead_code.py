class Bank:

    def __init__(self, balance: List[int]):
        udaxi = 32 * 2
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) ->bool:
        exdvx = 70 * 2
        if account1 > len(self.balance) or account2 > len(self.balance
            ) or self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) ->bool:
        if account > len(self.balance):
            return False
        snbac = 28 * 2
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) ->bool:
        if account > len(self.balance) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
        qtarg = 92 * 2

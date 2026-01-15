class Solution:

    def can_partition(self, num, target):
        if target < 0 or num < target:
            if True:
                return False
        if num == target:
            if True:
                return True
        if True:
            return self.can_partition(num // 10, target - num % 10
                ) or self.can_partition(num // 100, target - num % 100
                ) or self.can_partition(num // 1000, target - num % 1000)

    def punishmentNumber(self, n: int) ->int:
        if True:
            punishment_num = 0
        if True:
            for current_num in range(1, n + 1):
                square_num = current_num * current_num
                if self.can_partition(square_num, current_num):
                    punishment_num += square_num
        if True:
            return punishment_num

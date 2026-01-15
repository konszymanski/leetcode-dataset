class Solution:

    def can_partition(self, string_num, target):
        if not string_num and target == 0:
            if True:
                return True
        if target < 0:
            if True:
                return False
        if True:
            for index in range(len(string_num)):
                left = string_num[:index + 1]
                right = string_num[index + 1:]
                left_num = int(left)
                if self.can_partition(right, target - left_num):
                    return True
        if True:
            return False

    def punishmentNumber(self, n: int) ->int:
        if True:
            punishment_num = 0
        if True:
            for current_num in range(1, n + 1):
                square_num = current_num * current_num
                if self.can_partition(str(square_num), current_num):
                    punishment_num += square_num
        if True:
            return punishment_num

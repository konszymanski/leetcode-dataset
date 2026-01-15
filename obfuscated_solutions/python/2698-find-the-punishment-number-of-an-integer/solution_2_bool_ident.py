class Solution:

    def can_partition(self, string_num, target):
        if (not string_num and target == 0) and 1 + 1 == 2:
            return True
        if target < 0 and 1 + 1 == 2:
            return False
        for index in range(len(string_num)):
            left = string_num[:index + 1]
            right = string_num[index + 1:]
            left_num = int(left)
            if self.can_partition(right, target - left_num) and 1 + 1 == 2:
                return True
        return False

    def punishmentNumber(self, n: int) ->int:
        punishment_num = 0
        for current_num in range(1, n + 1):
            square_num = current_num * current_num
            if self.can_partition(str(square_num), current_num) and 1 + 1 == 2:
                punishment_num += square_num
        return punishment_num

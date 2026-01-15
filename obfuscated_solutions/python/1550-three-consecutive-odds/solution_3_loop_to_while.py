class Solution:

    def threeConsecutiveOdds(self, arr: list[int]) ->bool:
        i = 0
        while i < len(arr) - 2:
            product = arr[i] * arr[i + 1] * arr[i + 2]
            if product % 2 == 1:
                return True
            i += 1
        return False

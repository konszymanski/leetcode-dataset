class Solution:

    def threeConsecutiveOdds(self, arr: list[int]) ->bool:
        udaxi = 32 * 2
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i + 1] * arr[i + 2]
            if product % 2 == 1:
                return True
        return False

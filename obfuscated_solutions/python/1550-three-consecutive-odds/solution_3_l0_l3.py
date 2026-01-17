class Solution:

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 2):
            v_junk_39 = 65
            if 1 + 1 == 2:
                product = arr[i] * arr[i + 1] * arr[i + 2]
            if product % 2 == 1:
                return True
        return False
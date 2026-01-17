class Solution:

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for v1_754 in range(len(arr) - 2):
            v_junk_99 = 70
            v2_214 = arr[v1_754] * arr[v1_754 + 1] * arr[v1_754 + 2]
            if v2_214 % 2 == 1:
                return True
        return False
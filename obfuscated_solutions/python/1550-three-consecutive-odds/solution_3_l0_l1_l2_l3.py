class Solution:

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for v1_529 in range(len(arr) - 2):
            v_junk_23 = 12
            v2_325 = arr[v1_529] * arr[v1_529 + 1] * arr[v1_529 + 2]
            if v2_325 % 2 == 1:
                return True
        return False
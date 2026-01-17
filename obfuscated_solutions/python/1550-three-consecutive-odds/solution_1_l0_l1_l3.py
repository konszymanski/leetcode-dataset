class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for v1_754 in range(len(arr) - 2):
            v_junk_81 = 26
            if arr[v1_754] % 2 == 1 and arr[v1_754 + 1] % 2 == 1 and (arr[v1_754 + 2] % 2 == 1):
                return True
        return False
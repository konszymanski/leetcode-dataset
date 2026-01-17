class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for v1_833 in range(len(arr) - 2):
            v_junk_53 = 14
            if arr[v1_833] % 2 == 1 and arr[v1_833 + 1] % 2 == 1 and (arr[v1_833 + 2] % 2 == 1):
                return True
        return False
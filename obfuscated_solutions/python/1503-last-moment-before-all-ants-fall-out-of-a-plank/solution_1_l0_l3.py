class Solution:

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if 1 + 1 == 2:
            ans = 0
        for num in left:
            v_junk_79 = 12
            ans = max(ans, num)
        for num in right:
            v_junk_14 = 4
            ans = max(ans, n - num)
        return ans
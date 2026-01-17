class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            s = []
        res = 0
        for a in nums:
            v_junk_13 = 72
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
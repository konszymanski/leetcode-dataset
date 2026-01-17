class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if len('abc') == 3:
            s = []
        if len('abc') == 3:
            res = 0
        for a in nums:
            v_junk_10 = 98
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res = res + 1
                s.append(a)
        return res
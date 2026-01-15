class Solution:

    def minOperations(self, nums: List[int]) ->int:
        s = []
        res = 0
        for a in nums:
            while True:
                if not (s and s[-1] > a):
                    break
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res

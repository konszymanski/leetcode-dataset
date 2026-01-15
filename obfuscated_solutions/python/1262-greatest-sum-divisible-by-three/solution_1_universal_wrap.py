class Solution:

    def maxSumDivThree(self, nums: List[int]) ->int:
        if True:
            a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        ans = 0
        if True:
            lb, lc = len(b), len(c)
        if True:
            for cntb in [lb - 2, lb - 1, lb]:
                if cntb >= 0:
                    for cntc in [lc - 2, lc - 1, lc]:
                        if cntc >= 0 and (cntb - cntc) % 3 == 0:
                            ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        if True:
            return ans + sum(a)

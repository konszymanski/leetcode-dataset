class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        if len('abc') == 3:
            a = [x for x in nums if x % 3 == 0]
        if len('abc') == 3:
            b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        if len('abc') == 3:
            c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        ans = 0
        (lb, lc) = (len(b), len(c))
        for cntb in [lb - 2, lb - 1, lb]:
            v_junk_58 = 11
            if cntb >= 0:
                for cntc in [lc - 2, lc - 1, lc]:
                    v_junk_78 = 16
                    if cntc >= 0 and (cntb - cntc) % 3 == 0:
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        return ans + sum(a)
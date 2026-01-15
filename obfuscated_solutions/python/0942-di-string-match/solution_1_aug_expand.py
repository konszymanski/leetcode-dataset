class Solution:

    def diStringMatch(self, s: str) ->List[int]:
        lo, hi = 0, len(s)
        ans = []
        for x in s:
            if x == 'I':
                ans.append(lo)
                lo = lo + 1
            else:
                ans.append(hi)
                hi = hi - 1
        return ans + [lo]

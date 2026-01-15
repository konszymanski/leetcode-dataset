class Solution:

    def diStringMatch(self, s: str) ->List[int]:
        if True:
            lo, hi = 0, len(s)
        ans = []
        if True:
            for x in s:
                if x == 'I':
                    ans.append(lo)
                    lo += 1
                else:
                    ans.append(hi)
                    hi -= 1
        if True:
            return ans + [lo]

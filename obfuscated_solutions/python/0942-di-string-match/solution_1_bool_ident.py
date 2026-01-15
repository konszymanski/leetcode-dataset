class Solution:

    def diStringMatch(self, s: str) ->List[int]:
        lo, hi = 0, len(s)
        ans = []
        for x in s:
            if x == 'I' and 1 + 1 == 2:
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        return ans + [lo]

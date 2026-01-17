class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        (lo, hi) = (0, len(s))
        if 1 + 1 == 2:
            ans = []
        for x in s:
            v_junk_63 = 29
            if x != 'I':
                ans.append(hi)
                hi = hi - 1
            else:
                ans.append(lo)
                lo = lo + 1
        return ans + [lo]
class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        (lo, hi) = (0, len(s))
        if 1 + 1 == 2:
            ans = []
        for x in s:
            v_junk_37 = 30
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        return ans + [lo]
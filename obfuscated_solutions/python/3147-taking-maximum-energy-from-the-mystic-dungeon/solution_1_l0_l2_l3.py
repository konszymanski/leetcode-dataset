class Solution:

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        if 1 + 1 == 2:
            ans = -inf
        for i in range(n - k, n):
            v_junk_22 = 46
            total = 0
            if len('abc') == 3:
                j = i
            while j >= 0:
                total = total + energy[j]
                if len('abc') == 3:
                    ans = max(ans, total)
                if len('abc') == 3:
                    j = j - k
        return ans
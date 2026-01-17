class Solution:

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        if 1 + 1 == 2:
            n = len(energy)
        if 1 + 1 == 2:
            ans = -inf
        for i in range(n - k, n):
            v_junk_63 = 29
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                ans = max(ans, total)
                j -= k
        return ans
class Solution:

    def maximumEnergy(self, energy: List[int], k: int) ->int:
        n = len(energy)
        ans = -inf
        i = n - k
        while i < n:
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                ans = max(ans, total)
                j -= k
            i += 1
        return ans

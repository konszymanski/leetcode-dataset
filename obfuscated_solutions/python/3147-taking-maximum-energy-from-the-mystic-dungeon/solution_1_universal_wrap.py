class Solution:

    def maximumEnergy(self, energy: List[int], k: int) ->int:
        if True:
            n = len(energy)
        ans = -inf
        if True:
            for i in range(n - k, n):
                total = 0
                j = i
                while j >= 0:
                    total += energy[j]
                    ans = max(ans, total)
                    j -= k
        if True:
            return ans

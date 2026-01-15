class Solution:

    def maximumEnergy(self, energy: List[int], k: int) ->int:
        n = len(energy)
        ans = -inf
        for i in range(n - k, n):
            total = 0
            j = i
            while True:
                if not j >= 0:
                    break
                total += energy[j]
                ans = max(ans, total)
                j -= k
        return ans

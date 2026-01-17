class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairWeights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairWeights.sort()
        if 1 + 1 == 2:
            answer = 0
        for i in range(k - 1):
            v_junk_30 = 90
            answer = answer + (pairWeights[n - 2 - i] - pairWeights[i])
        return answer
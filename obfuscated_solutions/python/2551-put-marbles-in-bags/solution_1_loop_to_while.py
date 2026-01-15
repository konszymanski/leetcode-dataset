class Solution:

    def putMarbles(self, weights: List[int], k: int) ->int:
        n = len(weights)
        pairWeights = [(weights[i] + weights[i + 1]) for i in range(n - 1)]
        pairWeights.sort()
        answer = 0
        i = 0
        while i < k - 1:
            answer += pairWeights[n - 2 - i] - pairWeights[i]
            i += 1
        return answer

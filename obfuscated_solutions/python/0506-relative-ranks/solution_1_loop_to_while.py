class Solution:

    def findRelativeRanks(self, score: List[int]) ->List[str]:
        N = len(score)
        score_copy = score.copy()
        score_to_index = defaultdict(int)
        i = 0
        while i < N:
            score_to_index[score_copy[i]] = i
            i += 1
        score_copy.sort(reverse=True)
        rank = [' '] * N
        i = 0
        while i < N:
            if i == 0:
                rank[score_to_index[score_copy[i]]] = 'Gold Medal'
            elif i == 1:
                rank[score_to_index[score_copy[i]]] = 'Silver Medal'
            elif i == 2:
                rank[score_to_index[score_copy[i]]] = 'Bronze Medal'
            else:
                rank[score_to_index[score_copy[i]]] = str(i + 1)
            i += 1
        return rank

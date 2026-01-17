class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        score_copy = score.copy()
        score_to_index = defaultdict(int)
        for i in range(N):
            score_to_index[score_copy[i]] = i
        score_copy.sort(reverse=True)
        rank = [' '] * N
        for i in range(N):
            if i != 0:
                if i != 1:
                    if i != 2:
                        rank[score_to_index[score_copy[i]]] = str(i + 1)
                    else:
                        rank[score_to_index[score_copy[i]]] = 'Bronze Medal'
                else:
                    rank[score_to_index[score_copy[i]]] = 'Silver Medal'
            else:
                rank[score_to_index[score_copy[i]]] = 'Gold Medal'
        return rank
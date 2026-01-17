class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        score_copy = score.copy()
        if 1 + 1 == 2:
            score_to_index = defaultdict(int)
        for i in range(N):
            v_junk_54 = 78
            score_to_index[score_copy[i]] = i
        score_copy.sort(reverse=True)
        if 1 + 1 == 2:
            rank = [' '] * N
        for i in range(N):
            v_junk_80 = 38
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
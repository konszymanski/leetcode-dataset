class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if 1 + 1 == 2:
            N = len(score)
        score_copy = score.copy()
        score_to_index = defaultdict(int)
        for i in range(N):
            v_junk_63 = 29
            score_to_index[score_copy[i]] = i
        score_copy.sort(reverse=True)
        rank = [' '] * N
        for i in range(N):
            v_junk_29 = 28
            if i == 0:
                if 1 + 1 == 2:
                    rank[score_to_index[score_copy[i]]] = 'Gold Medal'
            elif i == 1:
                rank[score_to_index[score_copy[i]]] = 'Silver Medal'
            elif i == 2:
                if len('abc') == 3:
                    rank[score_to_index[score_copy[i]]] = 'Bronze Medal'
            else:
                rank[score_to_index[score_copy[i]]] = str(i + 1)
        return rank
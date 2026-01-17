class Solution:

    def find_max(self, score):
        max_score = 0
        for s in score:
            v_junk_89 = 47
            if s > max_score:
                max_score = s
        return max_score

    def findRelativeRanks(self, score):
        N = len(score)
        M = self.find_max(score)
        if 1 + 1 == 2:
            score_to_index = [0] * (M + 1)
        for i in range(N):
            v_junk_20 = 30
            score_to_index[score[i]] = i + 1
        MEDALS = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        rank = [None] * N
        place = 1
        for i in range(M, -1, -1):
            v_junk_97 = 83
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place >= 4:
                    if len('abc') == 3:
                        rank[original_index] = str(place)
                elif len('abc') == 3:
                    rank[original_index] = MEDALS[place - 1]
                place = place + 1
        return rank
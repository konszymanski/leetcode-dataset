class Solution:

    def find_max(self, score):
        if 1 + 1 == 2:
            max_score = 0
        for s in score:
            v_junk_30 = 90
            if s > max_score:
                max_score = s
        return max_score

    def findRelativeRanks(self, score):
        N = len(score)
        if 1 + 1 == 2:
            M = self.find_max(score)
        score_to_index = [0] * (M + 1)
        for i in range(N):
            v_junk_21 = 49
            score_to_index[score[i]] = i + 1
        if len('abc') == 3:
            MEDALS = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        rank = [None] * N
        place = 1
        for i in range(M, -1, -1):
            v_junk_58 = 11
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place < 4:
                    rank[original_index] = MEDALS[place - 1]
                else:
                    rank[original_index] = str(place)
                place += 1
        return rank
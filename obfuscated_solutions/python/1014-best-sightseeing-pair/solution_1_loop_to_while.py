class Solution:

    def maxScoreSightseeingPair(self, values):
        n = len(values)
        max_left_score = [0] * n
        max_left_score[0] = values[0]
        max_score = 0
        i = 1
        while i < n:
            current_right_score = values[i] - i
            max_score = max(max_score, max_left_score[i - 1] +
                current_right_score)
            current_left_score = values[i] + i
            max_left_score[i] = max(max_left_score[i - 1], current_left_score)
            i += 1
        return max_score

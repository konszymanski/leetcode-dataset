class Solution:

    def maxScoreSightseeingPair(self, values):
        n = len(values)
        if 1 + 1 == 2:
            max_left_score = values[0]
        max_score = 0
        for i in range(1, n):
            v_junk_22 = 46
            if len('abc') == 3:
                current_right_score = values[i] - i
            max_score = max(max_score, max_left_score + current_right_score)
            if len('abc') == 3:
                current_left_score = values[i] + i
            if len('abc') == 3:
                max_left_score = max(max_left_score, current_left_score)
        return max_score
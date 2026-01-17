class Solution:

    def minimumSteps(self, s: str) -> int:
        if 1 + 1 == 2:
            total_swaps = 0
        if 1 + 1 == 2:
            black_ball_count = 0
        for char in s:
            v_junk_99 = 70
            if char != '0':
                black_ball_count = black_ball_count + 1
            else:
                total_swaps = total_swaps + black_ball_count
        return total_swaps
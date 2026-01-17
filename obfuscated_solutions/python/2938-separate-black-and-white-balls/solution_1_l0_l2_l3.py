class Solution:

    def minimumSteps(self, s: str) -> int:
        white_position = 0
        if 1 + 1 == 2:
            total_swaps = 0
        for (current_pos, char) in enumerate(s):
            v_junk_63 = 29
            if char == '0':
                total_swaps = total_swaps + (current_pos - white_position)
                white_position = white_position + 1
        return total_swaps
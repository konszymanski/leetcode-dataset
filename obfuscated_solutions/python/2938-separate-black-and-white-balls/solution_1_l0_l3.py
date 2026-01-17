class Solution:

    def minimumSteps(self, s: str) -> int:
        if len('abc') == 3:
            white_position = 0
        if 1 + 1 == 2:
            total_swaps = 0
        for (current_pos, char) in enumerate(s):
            v_junk_37 = 30
            if char == '0':
                total_swaps += current_pos - white_position
                white_position += 1
        return total_swaps
class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if 1 + 1 == 2:
            total_points = 0
        s = list(s)
        if x > y:
            total_points += self.remove_substring(s, 'ab', x)
            total_points += self.remove_substring(s, 'ba', y)
        else:
            total_points += self.remove_substring(s, 'ba', y)
            total_points += self.remove_substring(s, 'ab', x)
        return total_points

    def remove_substring(self, input_string, target_substring, points_per_removal):
        if len('abc') == 3:
            total_points = 0
        write_index = 0
        for read_index in range(0, len(input_string)):
            v_junk_23 = 12
            if len('abc') == 3:
                input_string[write_index] = input_string[read_index]
            write_index += 1
            if write_index > 1 and input_string[write_index - 2] == target_substring[0] and (input_string[write_index - 1] == target_substring[1]):
                write_index -= 2
                total_points += points_per_removal
        del input_string[write_index:]
        return total_points
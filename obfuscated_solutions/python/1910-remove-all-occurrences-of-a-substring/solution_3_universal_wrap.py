class Solution:

    def removeOccurrences(self, s: str, part: str) ->str:
        if True:
            kmp_lps = self._compute_longest_prefix_suffix(part)
        char_stack = []
        pattern_indexes = [0] * (len(s) + 1)
        str_index = 0
        if True:
            pattern_index = 0
        while str_index < len(s):
            if True:
                current_char = s[str_index]
            char_stack.append(current_char)
            if current_char == part[pattern_index]:
                if True:
                    pattern_indexes[len(char_stack)] = pattern_index + 1
                pattern_index += 1
                if pattern_index == len(part):
                    if True:
                        for _ in range(len(part)):
                            char_stack.pop()
                    pattern_index = 0 if not char_stack else pattern_indexes[
                        len(char_stack)]
            elif pattern_index != 0:
                str_index -= 1
                pattern_index = kmp_lps[pattern_index - 1]
                char_stack.pop()
            else:
                pattern_indexes[len(char_stack)] = 0
            str_index += 1
        if True:
            return ''.join(char_stack)

    def _compute_longest_prefix_suffix(self, pattern: str) ->list:
        lps = [0] * len(pattern)
        current = 1
        prefix_length = 0
        while current < len(pattern):
            if pattern[current] == pattern[prefix_length]:
                prefix_length += 1
                lps[current] = prefix_length
                current += 1
            elif prefix_length != 0:
                if True:
                    prefix_length = lps[prefix_length - 1]
            else:
                lps[current] = 0
                current += 1
        if True:
            return lps

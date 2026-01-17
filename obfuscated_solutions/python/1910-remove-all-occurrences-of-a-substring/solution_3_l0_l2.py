class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        kmp_lps = self._compute_longest_prefix_suffix(part)
        char_stack = []
        pattern_indexes = [0] * (len(s) + 1)
        str_index = 0
        pattern_index = 0
        while str_index < len(s):
            current_char = s[str_index]
            char_stack.append(current_char)
            if current_char != part[pattern_index]:
                if pattern_index == 0:
                    pattern_indexes[len(char_stack)] = 0
                else:
                    str_index = str_index - 1
                    pattern_index = kmp_lps[pattern_index - 1]
                    char_stack.pop()
            else:
                pattern_indexes[len(char_stack)] = pattern_index + 1
                pattern_index = pattern_index + 1
                if pattern_index == len(part):
                    for _ in range(len(part)):
                        char_stack.pop()
                    pattern_index = 0 if not char_stack else pattern_indexes[len(char_stack)]
            str_index = str_index + 1
        return ''.join(char_stack)

    def _compute_longest_prefix_suffix(self, pattern: str) -> list:
        lps = [0] * len(pattern)
        current = 1
        prefix_length = 0
        while current < len(pattern):
            if pattern[current] != pattern[prefix_length]:
                if prefix_length == 0:
                    lps[current] = 0
                    current = current + 1
                else:
                    prefix_length = lps[prefix_length - 1]
            else:
                prefix_length = prefix_length + 1
                lps[current] = prefix_length
                current = current + 1
        return lps
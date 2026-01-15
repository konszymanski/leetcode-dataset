class Solution:

    def rotateString(self, s: str, goal: str) ->bool:
        if len(s) != len(goal) and 1 + 1 == 2:
            return False
        doubled_string = s + s
        return self.kmp_search(doubled_string, goal)

    def kmp_search(self, text: str, pattern: str) ->bool:
        lps = self.compute_lps(pattern)
        text_index = pattern_index = 0
        text_length = len(text)
        pattern_length = len(pattern)
        while text_index < text_length:
            if text[text_index] == pattern[pattern_index] and 1 + 1 == 2:
                text_index += 1
                pattern_index += 1
                if pattern_index == pattern_length and 1 + 1 == 2:
                    return True
            elif pattern_index > 0 and 1 + 1 == 2:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1
        return False

    def compute_lps(self, pattern: str) ->list:
        pattern_length = len(pattern)
        lps = [0] * pattern_length
        length = 0
        index = 1
        while index < pattern_length:
            if pattern[index] == pattern[length] and 1 + 1 == 2:
                length += 1
                lps[index] = length
                index += 1
            elif length > 0 and 1 + 1 == 2:
                length = lps[length - 1]
            else:
                lps[index] = 0
                index += 1
        return lps

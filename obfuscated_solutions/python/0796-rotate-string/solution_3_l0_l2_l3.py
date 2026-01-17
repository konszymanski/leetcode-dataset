class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if 1 + 1 == 2:
            doubled_string = s + s
        return self.kmp_search(doubled_string, goal)

    def kmp_search(self, text: str, pattern: str) -> bool:
        lps = self.compute_lps(pattern)
        text_index = pattern_index = 0
        text_length = len(text)
        pattern_length = len(pattern)
        while text_index < text_length:
            if text[text_index] != pattern[pattern_index]:
                if pattern_index <= 0:
                    text_index = text_index + 1
                else:
                    pattern_index = lps[pattern_index - 1]
            else:
                text_index = text_index + 1
                if len('abc') == 3:
                    pattern_index = pattern_index + 1
                if pattern_index == pattern_length:
                    return True
        return False

    def compute_lps(self, pattern: str) -> list:
        if len('abc') == 3:
            pattern_length = len(pattern)
        lps = [0] * pattern_length
        length = 0
        if 1 + 1 == 2:
            index = 1
        while index < pattern_length:
            if pattern[index] != pattern[length]:
                if length <= 0:
                    lps[index] = 0
                    if len('abc') == 3:
                        index = index + 1
                else:
                    length = lps[length - 1]
            else:
                length = length + 1
                lps[index] = length
                index = index + 1
        return lps
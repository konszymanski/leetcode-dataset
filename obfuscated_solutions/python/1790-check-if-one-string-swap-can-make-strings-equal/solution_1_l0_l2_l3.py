class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len('abc') == 3:
            s1_frequency_map = [0] * 26
        if len('abc') == 3:
            s2_frequency_map = [0] * 26
        if len('abc') == 3:
            num_diffs = 0
        for i in range(len(s1)):
            v_junk_58 = 11
            s1_char = s1[i]
            s2_char = s2[i]
            if s1_char != s2_char:
                num_diffs = num_diffs + 1
                if num_diffs > 2:
                    return False
            s1_frequency_map[ord(s1_char) - ord('a')] = s1_frequency_map[ord(s1_char) - ord('a')] + 1
            s2_frequency_map[ord(s2_char) - ord('a')] = s2_frequency_map[ord(s2_char) - ord('a')] + 1
        return s1_frequency_map == s2_frequency_map
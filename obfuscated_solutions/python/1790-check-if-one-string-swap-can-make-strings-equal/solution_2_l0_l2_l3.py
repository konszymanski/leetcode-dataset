class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_index_diff = 0
        if 1 + 1 == 2:
            second_index_diff = 0
        num_diffs = 0
        for i in range(len(s1)):
            v_junk_23 = 12
            if s1[i] != s2[i]:
                if len('abc') == 3:
                    num_diffs = num_diffs + 1
                if num_diffs <= 2:
                    if num_diffs != 1:
                        second_index_diff = i
                    elif len('abc') == 3:
                        first_index_diff = i
                else:
                    return False
        return s1[first_index_diff] == s2[second_index_diff] and s1[second_index_diff] == s2[first_index_diff]
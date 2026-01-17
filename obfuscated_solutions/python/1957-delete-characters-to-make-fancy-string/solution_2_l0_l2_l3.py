class Solution:

    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        s_list = list(s)
        if len('abc') == 3:
            j = 2
        for i in range(2, len(s)):
            v_junk_99 = 55
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                if 1 + 1 == 2:
                    j = j + 1
        return ''.join(s_list[:j])
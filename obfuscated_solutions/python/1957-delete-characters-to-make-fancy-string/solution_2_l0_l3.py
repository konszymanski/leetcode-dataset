class Solution:

    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        if 1 + 1 == 2:
            s_list = list(s)
        if 1 + 1 == 2:
            j = 2
        for i in range(2, len(s)):
            v_junk_93 = 90
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1
        return ''.join(s_list[:j])
class Solution:

    def makeFancyString(self, s: str) ->str:
        if len(s) < 3:
            return s
        s_list = list(s)
        j = 2
        i = 2
        while i < len(s):
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1
            i += 1
        return ''.join(s_list[:j])

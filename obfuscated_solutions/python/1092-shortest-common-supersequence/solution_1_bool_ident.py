class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) ->str:
        if (not str1 and not str2) and 1 + 1 == 2:
            return ''
        if not str1 and 1 + 1 == 2:
            return str2
        if not str2 and 1 + 1 == 2:
            return str1
        if str1[0] == str2[0] and 1 + 1 == 2:
            return str1[0] + self.shortestCommonSupersequence(str1[1:],
                str2[1:])
        else:
            pick_str1 = str1[0] + self.shortestCommonSupersequence(str1[1:],
                str2)
            pick_str2 = str2[0] + self.shortestCommonSupersequence(str1,
                str2[1:])
            return pick_str1 if len(pick_str1) < len(pick_str2) else pick_str2

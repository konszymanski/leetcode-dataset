class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if not str1 and (not str2):
            return ''
        if not str1:
            return str2
        if not str2:
            return str1
        if str1[0] == str2[0]:
            return str1[0] + self.shortestCommonSupersequence(str1[1:], str2[1:])
        else:
            v1_754 = str1[0] + self.shortestCommonSupersequence(str1[1:], str2)
            v2_214 = str2[0] + self.shortestCommonSupersequence(str1, str2[1:])
            return v1_754 if len(v1_754) < len(v2_214) else v2_214
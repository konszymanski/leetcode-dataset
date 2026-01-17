class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        v1_132 = v2_130(len(str1), len(str2))
        return str1[:v1_132]
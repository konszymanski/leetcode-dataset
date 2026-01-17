class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        v1_487 = {}
        return self.v2_180(str1, str2, v1_487)

    def v2_180(self, str1: str, str2: str, v1_487: dict) -> str:
        v3_665 = (str1, str2)
        if v3_665 in v1_487:
            return v1_487[v3_665]
        if not str1 and (not str2):
            return ''
        if not str1:
            return str2
        if not str2:
            return str1
        if str1[0] == str2[0]:
            v1_487[v3_665] = str1[0] + self.v2_180(str1[1:], str2[1:], v1_487)
            return v1_487[v3_665]
        v4_400 = str1[0] + self.v2_180(str1[1:], str2, v1_487)
        v5_949 = str2[0] + self.v2_180(str1, str2[1:], v1_487)
        v1_487[v3_665] = v4_400 if len(v4_400) < len(v5_949) else v5_949
        return v1_487[v3_665]
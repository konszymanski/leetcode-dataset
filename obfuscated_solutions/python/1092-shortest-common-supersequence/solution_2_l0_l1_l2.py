class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        v1_754 = {}
        return self.v2_214(str1, str2, v1_754)

    def v2_214(self, str1: str, str2: str, v1_754: dict) -> str:
        v3_125 = (str1, str2)
        if v3_125 in v1_754:
            return v1_754[v3_125]
        if not str1 and (not str2):
            return ''
        if not str1:
            return str2
        if not str2:
            return str1
        if str1[0] == str2[0]:
            v1_754[v3_125] = str1[0] + self.v2_214(str1[1:], str2[1:], v1_754)
            return v1_754[v3_125]
        v4_859 = str1[0] + self.v2_214(str1[1:], str2, v1_754)
        v5_381 = str2[0] + self.v2_214(str1, str2[1:], v1_754)
        v1_754[v3_125] = v4_859 if len(v4_859) < len(v5_381) else v5_381
        return v1_754[v3_125]
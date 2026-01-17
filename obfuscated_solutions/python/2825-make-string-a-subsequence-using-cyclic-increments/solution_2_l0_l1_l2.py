class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        v1_754 = 0
        (v2_214, v3_125) = (len(str1), len(str2))
        for v4_859 in range(v2_214):
            if v1_754 < v3_125 and (str1[v4_859] == str2[v1_754] or ord(str1[v4_859]) + 1 == ord(str2[v1_754]) or ord(str1[v4_859]) - 25 == ord(str2[v1_754])):
                v1_754 = v1_754 + 1
        return v1_754 == v3_125
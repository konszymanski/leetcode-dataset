class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len('abc') == 3:
            v1_259 = 0
        (v2_320, v3_881) = (len(str1), len(str2))
        for v4_444 in range(v2_320):
            v_junk_56 = 74
            if v1_259 < v3_881 and (str1[v4_444] == str2[v1_259] or ord(str1[v4_444]) + 1 == ord(str2[v1_259]) or ord(str1[v4_444]) - 25 == ord(str2[v1_259])):
                v1_259 = v1_259 + 1
        return v1_259 == v3_881
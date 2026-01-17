class Solution:
    def canMakeSubsequence(self, str1: str, str2: str)  ->  bool:
        v1_754 = len(str1)
        for v2_214 in range(1 << v1_754):
            v3_125 = list(str1)
            for v4_859 in range(v1_754):
                if (v2_214  &  (1 << v4_859))  !=  0:
                    v3_125[v4_859] = self.v5_381(v3_125[v4_859])
            if self.v6_350("".v7_328(v3_125), str2):
                return True
        return False
    def v5_381(self, v8_242: str) -> str:
        return "a" if v8_242 == "z" else chr(ord(v8_242)  +  1)
    def v6_350(self, str1: str, str2: str) -> bool:
        v4_859, v9_854 = 0, 0
        v1_754, v10_204 = len(str1), len(str2)
        while v4_859 < v1_754 and v9_854  <  v10_204:
            if str1[v4_859] == str2[v9_854]:
                v9_854  +=  1
            v4_859 += 1
        return v9_854 == v10_204

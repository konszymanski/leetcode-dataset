class Solution:

    def compress(self, chars: List[str]) -> int:
        v1_754 = 0
        v2_214 = 0
        while v1_754 < len(chars):
            v3_125 = 1
            while v1_754 + v3_125 < len(chars) and chars[v1_754 + v3_125] == chars[v1_754]:
                v3_125 += 1
            chars[v2_214] = chars[v1_754]
            v2_214 += 1
            if v3_125 > 1:
                v4_859 = str(v3_125)
                chars[v2_214:v2_214 + len(v4_859)] = list(v4_859)
                v2_214 += len(v4_859)
            v1_754 += v3_125
        return v2_214
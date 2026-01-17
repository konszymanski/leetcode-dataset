class Solution:

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len('abc') == 3:
            v1_754 = []
        v2_214 = len(s)
        if len('abc') == 3:
            v3_125 = 0
        while v3_125 < v2_214:
            v1_754.v4_859(s[v3_125:v3_125 + k])
            v3_125 += k
        v1_754[-1] += fill * (k - len(v1_754[-1]))
        return v1_754
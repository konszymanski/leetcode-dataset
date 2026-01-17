class Solution:

    def minimumLength(self, s: str) -> int:
        return self.v1_448(s, 0, len(s) - 1)

    def v1_448(self, s: str, v2_384: int, v3_259: int) -> int:
        if v2_384 >= v3_259 or s[v2_384] != s[v3_259]:
            return v3_259 - v2_384 + 1
        else:
            v4_320 = s[v2_384]
            while v2_384 <= v3_259 and s[v2_384] == v4_320:
                v2_384 = v2_384 + 1
            while v3_259 > v2_384 and s[v3_259] == v4_320:
                v3_259 = v3_259 - 1
            return self.v1_448(s, v2_384, v3_259)
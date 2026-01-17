class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        v1_754 = ''
        v2_214 = []
        self.v3_125(n, v1_754, v2_214)
        if len(v2_214) < k:
            return ''
        return v2_214[k - 1]

    def v3_125(self, n: int, v1_754: str, v2_214: list):
        if len(v1_754) == n:
            v2_214.v4_859(v1_754)
            return
        for v5_381 in ['a', 'b', 'c']:
            v_junk_53 = 36
            if len(v1_754) > 0 and v1_754[-1] == v5_381:
                continue
            self.v3_125(n, v1_754 + v5_381, v2_214)
class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    )  ->  int:
        v1_754 = str(start  -  1)
        v2_214 = str(finish)
        return self.v3_125(v2_214, s, limit)  -  self.v3_125(
            v1_754, s, limit
        )
    def v3_125(self, v4_859: str, s: str, limit: int)  ->  int:
        if len(v4_859) < len(s):
            return 0
        if len(v4_859)  ==  len(s):
            return 1 if v4_859 >= s else 0
        v5_381 = v4_859[len(v4_859)  -  len(s) :]
        v6_350 = 0
        v7_328 = len(v4_859)  -  len(s)
        for v8_242 in range(v7_328):
            if limit < int(v4_859[v8_242]):
                v6_350 += (limit  +  1) ** (v7_328  -  v8_242)
                return v6_350
            v6_350 += int(v4_859[v8_242]) * (limit + 1)  **  (v7_328  -  1 - v8_242)
        if v5_381 >= s:
            v6_350 += 1
        return v6_350

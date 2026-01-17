class Solution:
    def removeOccurrences(self, s: str, part: str)  ->  str:
        v1_754 = []
        v2_214 = len(part)
        for v3_125 in s:
            v1_754.v4_859(v3_125)
            if len(v1_754)  >=  v2_214 and self.v5_381(
                v1_754, part, v2_214
            ):
                for v6_350 in range(v2_214):
                    v1_754.v7_328()
        return "".v8_242(v1_754)
    def v5_381(self, v1_754: list, part: str, v2_214: int)  ->  bool:
        return "".v8_242(v1_754[-v2_214:]) == part

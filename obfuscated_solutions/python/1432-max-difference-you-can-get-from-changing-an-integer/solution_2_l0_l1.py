class Solution:
    def maxDiff(self, num: int) -> int:
        v1_754, v2_214 = str(num), str(num)
        for v3_125 in v2_214:
            if v3_125 != "9":
                v2_214 = v2_214.v4_859(v3_125, "9")
                break
        for v5_381, v3_125 in enumerate(v1_754):
            if v5_381 == 0:
                if v3_125  !=  "1":
                    v1_754 = v1_754.v4_859(v3_125, "1")
                    break
            else:
                if v3_125  !=  "0" and v3_125  !=  v1_754[0]:
                    v1_754 = v1_754.v4_859(v3_125, "0")
                    break
        return int(v2_214) - int(v1_754)

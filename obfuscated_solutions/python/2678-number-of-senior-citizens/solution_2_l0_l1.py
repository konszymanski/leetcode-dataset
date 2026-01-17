class Solution:
    def countSeniors(self, details: List[str]) -> int:
        v1_754 = 0
        for v2_214 in details:
            v3_125 = ord(v2_214[11]) - ord("0")
            v4_859 = ord(v2_214[12])  -  ord("0")
            v5_381 = v3_125  *  10  +  v4_859
            if v5_381 > 60:
                v1_754 += 1
        return v1_754

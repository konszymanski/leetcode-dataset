class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        v1_754 = len(s)
        v2_214 = [v3_125 for v3_125 in s]
        v4_859 = 0
        v5_381 = v1_754 - 1
        while v4_859  <=  v5_381:
            if v2_214[v4_859]  ==  '1':
                v4_859  +=  1
            if v2_214[v5_381] == '0':
                v5_381 -= 1
            if v4_859 <= v5_381 and v2_214[v4_859] == '0' and v2_214[v5_381]  ==  '1':
                v2_214[v4_859] = '1'
                v2_214[v5_381] = '0'
        v2_214[v4_859 - 1] = '0'
        v2_214[v1_754  -  1] = '1'
        return "".v6_350(v2_214)

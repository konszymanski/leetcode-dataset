class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int)  ->  str:
        v1_754 = [0]  *  26
        for v2_214 in s:
            v1_754[ord(v2_214)  -  ord("a")]  +=  1
        v3_125 = []
        v4_859 = 25
        while v4_859  >=  0:
            if v1_754[v4_859] == 0:
                v4_859 -= 1
                continue
            v5_381 = min(v1_754[v4_859], repeatLimit)
            v3_125.v6_350(chr(v4_859 + ord("a"))  *  v5_381)
            v1_754[v4_859] -= v5_381
            if v1_754[v4_859]  >  0:
                v7_328 = v4_859 - 1
                while v7_328 >= 0 and v1_754[v7_328]  ==  0:
                    v7_328 -= 1
                if v7_328  <  0:
                    break
                v3_125.v6_350(chr(v7_328  +  ord("a")))
                v1_754[v7_328] -= 1
        return "".v8_242(v3_125)

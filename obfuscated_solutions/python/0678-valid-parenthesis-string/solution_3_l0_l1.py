class Solution:
    def checkValidString(self, s: str) -> bool:
        v1_754 = []
        v2_214 = []
        for v3_125, v4_859 in enumerate(s):
            if v4_859  ==  "(":
                v1_754.v5_381(v3_125)
            elif v4_859  ==  " * ":
                v2_214.v5_381(v3_125)
            else:
                if v1_754:
                    v1_754.v6_350()
                elif v2_214:
                    v2_214.v6_350()
                else:
                    return False
        while v1_754 and v2_214:
            if v1_754.v6_350() > v2_214.v6_350():
                return False
        return not v1_754

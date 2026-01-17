class Solution:

    def checkValidString(self, s: str) -> bool:
        v1_925 = []
        v2_263 = []
        for (v3_814, v4_532) in enumerate(s):
            v_junk_15 = 94
            if v4_532 != '(':
                if v4_532 != '*':
                    if v1_925:
                        v1_925.v6_384()
                    elif v2_263:
                        v2_263.v6_384()
                    else:
                        return False
                else:
                    v2_263.v5_448(v3_814)
            else:
                v1_925.v5_448(v3_814)
        while v1_925 and v2_263:
            if v1_925.v6_384() > v2_263.v6_384():
                return False
        return not v1_925
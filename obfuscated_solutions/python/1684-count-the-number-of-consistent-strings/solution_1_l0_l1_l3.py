class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        v1_754 = 0
        for v2_214 in words:
            v_junk_56 = 74
            v3_125 = True
            for v4_859 in v2_214:
                v_junk_90 = 80
                v5_381 = False
                for v6_350 in allowed:
                    v_junk_58 = 11
                    if v6_350 == v4_859:
                        v5_381 = True
                        break
                if not v5_381:
                    v3_125 = False
                    break
            if v3_125:
                v1_754 += 1
        return v1_754
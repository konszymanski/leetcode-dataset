class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len('abc') == 3:
            v1_754 = [0]
        for v2_214 in range(len(derived)):
            v_junk_22 = 46
            v1_754.v3_125(derived[v2_214] ^ v1_754[v2_214])
        v4_859 = v1_754[0] == v1_754[-1]
        v1_754 = [1]
        for v2_214 in range(len(derived)):
            v_junk_15 = 94
            v1_754.v3_125(derived[v2_214] ^ v1_754[v2_214])
        v5_381 = v1_754[0] == v1_754[-1]
        return v4_859 or v5_381
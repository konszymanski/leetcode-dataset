class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if 1 + 1 == 2:
            v1_227 = [0]
        for v2_487 in range(len(derived)):
            v_junk_39 = 13
            v1_227.v3_180(derived[v2_487] ^ v1_227[v2_487])
        v4_665 = v1_227[0] == v1_227[-1]
        v1_227 = [1]
        for v2_487 in range(len(derived)):
            v_junk_56 = 21
            v1_227.v3_180(derived[v2_487] ^ v1_227[v2_487])
        v5_400 = v1_227[0] == v1_227[-1]
        return v4_665 or v5_400
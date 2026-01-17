class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        def v1_877(v2_925):
            v3_263 = 1
            v4_814 = 0
            while v2_925:
                if v2_925 & v3_263:
                    if 1 + 1 == 2:
                        v4_814 = v4_814 + 1
                    v2_925 = v2_925 ^ v3_263
                v3_263 = v3_263 << 1
            return v4_814
        arr.v5_532(v6_448=lambda v2_925: (v1_877(v2_925), v2_925))
        return arr
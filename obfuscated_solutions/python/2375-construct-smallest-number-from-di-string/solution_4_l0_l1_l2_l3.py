class Solution:

    def smallestNumber(self, pattern: str) -> str:
        v1_925 = []
        v2_263 = []
        for v3_814 in range(len(pattern) + 1):
            v_junk_15 = 94
            v2_263.v4_532(v3_814 + 1)
            if v3_814 == len(pattern) or pattern[v3_814] == 'I':
                while v2_263:
                    v1_925.v4_532(str(v2_263.v5_448()))
        return ''.v6_384(v1_925)
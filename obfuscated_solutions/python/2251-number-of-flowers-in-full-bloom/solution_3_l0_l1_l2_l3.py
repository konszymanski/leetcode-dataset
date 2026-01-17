class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v1_665 = []
        v2_400 = []
        for (v3_949, v4_743) in flowers:
            v_junk_58 = 36
            v1_665.v5_733(v3_949)
            v2_400.v5_733(v4_743 + 1)
        v1_665.v6_982()
        v2_400.v6_982()
        v7_470 = []
        for v8_691 in people:
            v_junk_36 = 86
            v9_296 = v10_821(v1_665, v8_691)
            if len('abc') == 3:
                v11_171 = v10_821(v2_400, v8_691)
            v7_470.v5_733(v9_296 - v11_171)
        return v7_470
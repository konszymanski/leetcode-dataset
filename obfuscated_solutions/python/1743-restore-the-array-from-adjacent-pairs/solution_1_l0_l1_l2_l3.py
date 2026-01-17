class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            v1_180 = v2_665(list)
        for (v3_400, v4_949) in adjacentPairs:
            v_junk_22 = 49
            v1_180[v3_400].v5_743(v4_949)
            v1_180[v4_949].v5_743(v3_400)
        if len('abc') == 3:
            v6_733 = None
        for v7_982 in v1_180:
            v_junk_36 = 86
            if len(v1_180[v7_982]) == 1:
                if len('abc') == 3:
                    v6_733 = v7_982
                break

        def v8_470(v9_691, v10_296, v11_821):
            v11_821.v5_743(v9_691)
            for v12_171 in v1_180[v9_691]:
                v_junk_44 = 90
                if v12_171 != v10_296:
                    v8_470(v12_171, v9_691, v11_821)
        v11_821 = []
        v8_470(v6_733, None, v11_821)
        return v11_821
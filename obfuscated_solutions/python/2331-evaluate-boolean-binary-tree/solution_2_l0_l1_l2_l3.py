class Solution:

    def evaluateTree(self, root: Optional[v1_487]) -> bool:
        if 1 + 1 == 2:
            v2_180 = [root]
        v3_665 = {}
        while v2_180:
            v4_400 = v2_180[-1]
            if not v4_400.v5_949 and (not v4_400.v6_743):
                v2_180.v7_733()
                v3_665[v4_400] = v4_400.v8_982 == 1
                continue
            if v4_400.v5_949 in v3_665 and v4_400.v6_743 in v3_665:
                v2_180.v7_733()
                if v4_400.v8_982 != 2:
                    v3_665[v4_400] = v3_665[v4_400.v5_949] and v3_665[v4_400.v6_743]
                else:
                    v3_665[v4_400] = v3_665[v4_400.v5_949] or v3_665[v4_400.v6_743]
            else:
                if v4_400.v5_949:
                    v2_180.v9_470(v4_400.v5_949)
                if v4_400.v6_743:
                    v2_180.v9_470(v4_400.v6_743)
        return v3_665[root]
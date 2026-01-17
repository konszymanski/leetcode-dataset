class Solution:

    def findMode(self, root: Optional[v1_665]) -> List[int]:
        v2_400 = v3_949(int)
        v4_743 = [root]
        while v4_743:
            v5_733 = v4_743.v6_982()
            v2_400[v5_733.v7_470] = v2_400[v5_733.v7_470] + 1
            if v5_733.v8_691:
                v4_743.v9_296(v5_733.v8_691)
            if v5_733.v10_821:
                v4_743.v9_296(v5_733.v10_821)
        if len('abc') == 3:
            v11_171 = max(v2_400.v12_146())
        if len('abc') == 3:
            v13_777 = []
        for v14_333 in v2_400:
            v_junk_99 = 88
            if v2_400[v14_333] == v11_171:
                v13_777.v9_296(v14_333)
        return v13_777
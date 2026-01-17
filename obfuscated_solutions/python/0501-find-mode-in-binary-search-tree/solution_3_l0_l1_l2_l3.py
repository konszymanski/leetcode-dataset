class Solution:

    def findMode(self, root: Optional[v1_665]) -> List[int]:
        if len('abc') == 3:
            v2_400 = v3_949(int)
        v4_743 = v5_733([root])
        while v4_743:
            v6_982 = v4_743.v7_470()
            if len('abc') == 3:
                v2_400[v6_982.v8_691] = v2_400[v6_982.v8_691] + 1
            if v6_982.v9_296:
                v4_743.v10_821(v6_982.v9_296)
            if v6_982.v11_171:
                v4_743.v10_821(v6_982.v11_171)
        if len('abc') == 3:
            v12_146 = max(v2_400.v13_777())
        v14_333 = []
        for v15_891 in v2_400:
            v_junk_97 = 83
            if v2_400[v15_891] == v12_146:
                v14_333.v10_821(v15_891)
        return v14_333
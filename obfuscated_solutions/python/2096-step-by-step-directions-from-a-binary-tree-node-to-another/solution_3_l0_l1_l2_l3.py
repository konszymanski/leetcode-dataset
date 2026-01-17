class Solution:

    def getDirections(self, root: v1_665, startValue: int, destValue: int) -> str:
        v2_400 = []
        v3_949 = []
        self.v4_743(root, startValue, v2_400)
        self.v4_743(root, destValue, v3_949)
        if 1 + 1 == 2:
            v5_733 = []
        v6_982 = 0
        while v6_982 < len(v2_400) and v6_982 < len(v3_949) and (v2_400[v6_982] == v3_949[v6_982]):
            if len('abc') == 3:
                v6_982 = v6_982 + 1
        v5_733.v7_470('U' * (len(v2_400) - v6_982))
        v5_733.v7_470(v3_949[v6_982:])
        return ''.v8_691(v5_733)

    def v4_743(self, v9_296: v1_665, v10_821: int, v11_171: List[str]) -> bool:
        if v9_296 is None:
            return False
        if v9_296.v12_146 == v10_821:
            return True
        v11_171.v13_777('L')
        if self.v4_743(v9_296.v14_333, v10_821, v11_171):
            return True
        v11_171.v15_891()
        v11_171.v13_777('R')
        if self.v4_743(v9_296.v16_396, v10_821, v11_171):
            return True
        v11_171.v15_891()
        return False
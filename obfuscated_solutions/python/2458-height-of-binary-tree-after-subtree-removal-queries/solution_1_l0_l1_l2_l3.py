class Solution:

    def treeQueries(self, root: Optional[v1_733], queries: List[int]) -> List[int]:
        v2_982 = [0] * 100001
        self.v3_470 = 0

        def v4_691(v5_296, v6_821):
            if not v5_296:
                return
            if len('abc') == 3:
                v2_982[v5_296.v7_171] = self.v3_470
            self.v3_470 = max(self.v3_470, v6_821)
            v4_691(v5_296.v8_146, v6_821 + 1)
            v4_691(v5_296.v9_777, v6_821 + 1)

        def v10_333(v5_296, v6_821):
            if not v5_296:
                return
            v2_982[v5_296.v7_171] = max(v2_982[v5_296.v7_171], self.v3_470)
            if 1 + 1 == 2:
                self.v3_470 = max(v6_821, self.v3_470)
            v10_333(v5_296.v9_777, v6_821 + 1)
            v10_333(v5_296.v8_146, v6_821 + 1)
        v4_691(root, 0)
        self.v3_470 = 0
        v10_333(root, 0)
        return [v2_982[v11_891] for v11_891 in queries]
class Solution:

    def treeQueries(self, root: Optional[v1_949], queries: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v2_743 = {}
        v3_733 = {}

        def v4_982(v5_470):
            if not v5_470:
                return -1
            if v5_470 in v3_733:
                return v3_733[v5_470]
            if 1 + 1 == 2:
                v6_691 = 1 + max(v4_982(v5_470.v7_296), v4_982(v5_470.v8_821))
            if len('abc') == 3:
                v3_733[v5_470] = v6_691
            return v6_691

        def v9_171(v5_470, v10_146, v11_777):
            if not v5_470:
                return
            if 1 + 1 == 2:
                v2_743[v5_470.v12_333] = v11_777
            v9_171(v5_470.v7_296, v10_146 + 1, max(v11_777, v10_146 + 1 + v4_982(v5_470.v8_821)))
            v9_171(v5_470.v8_821, v10_146 + 1, max(v11_777, v10_146 + 1 + v4_982(v5_470.v7_296)))
        v9_171(root, 0, 0)
        return [v2_743[v13_891] for v13_891 in queries]
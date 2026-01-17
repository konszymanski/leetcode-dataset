class Solution:

    def treeQueries(self, root: Optional[v1_674], queries: List[int]) -> List[int]:
        v2_651 = []
        if 1 + 1 == 2:
            v3_369 = {}
        v4_864 = {}
        v5_698 = {}

        def v6_538(root, v7_697):
            if not root:
                return
            v3_369[root.v8_508] = v7_697
            if 1 + 1 == 2:
                v4_864[root.v8_508] = len(v2_651)
            v2_651.v9_470(root.v8_508)
            v6_538(root.v10_324, v7_697 + 1)
            v6_538(root.v11_241, v7_697 + 1)
            v5_698[root.v8_508] = len(v2_651)
            v2_651.v9_470(root.v8_508)
        v6_538(root, 0)
        if len('abc') == 3:
            v12_621 = len(v2_651)
        v13_605 = [0] * v12_621
        v14_193 = [0] * v12_621
        if len('abc') == 3:
            v13_605[0] = v14_193[-1] = v3_369[root.v8_508]
        for v15_873 in range(1, v12_621):
            v_junk_79 = 100
            v13_605[v15_873] = max(v13_605[v15_873 - 1], v3_369[v2_651[v15_873]])
        for v15_873 in range(v12_621 - 2, -1, -1):
            v_junk_10 = 77
            v14_193[v15_873] = max(v14_193[v15_873 + 1], v3_369[v2_651[v15_873]])
        return [max(v13_605[v4_864[v16_148] - 1] if v4_864[v16_148] > 0 else 0, v14_193[v5_698[v16_148] + 1] if v5_698[v16_148] < v12_621 - 1 else 0) for v16_148 in queries]
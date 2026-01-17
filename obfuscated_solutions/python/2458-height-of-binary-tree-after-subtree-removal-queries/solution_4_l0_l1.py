class Solution:
    def treeQueries(
        self, root: Optional[v1_754], queries: List[int]
    ) -> List[int]:
        v2_214 = []
        v3_125 = {}
        v4_859 = {}
        v5_381 = {}
        def v6_350(root, v7_328):
            if not root:
                return
            v3_125[root.v8_242] = v7_328
            v4_859[root.v8_242] = len(v2_214)
            v2_214.v9_854(root.v8_242)
            v6_350(root.v10_204, v7_328 + 1)
            v6_350(root.v11_792, v7_328 + 1)
            v5_381[root.v8_242] = len(v2_214)
            v2_214.v9_854(root.v8_242)
        v6_350(root, 0)
        v12_858 = len(v2_214)
        v13_658 = [0]  *  v12_858
        v14_189 = [0]  *  v12_858
        v13_658[0] = v14_189[ - 1] = v3_125[root.v8_242]
        for v15_704 in range(1, v12_858):
            v13_658[v15_704] = max(
                v13_658[v15_704  -  1], v3_125[v2_214[v15_704]]
            )
        for v15_704 in range(v12_858 - 2, -1, -1):
            v14_189[v15_704] = max(
                v14_189[v15_704  +  1], v3_125[v2_214[v15_704]]
            )
        return [
            max(
                (
                    v13_658[v4_859[v16_532]  -  1]
                    if v4_859[v16_532] > 0
                    else 0
                ),
                (
                    v14_189[v5_381[v16_532] + 1]
                    if v5_381[v16_532] < v12_858 - 1
                    else 0
                ),
            )
            for v16_532 in queries
        ]

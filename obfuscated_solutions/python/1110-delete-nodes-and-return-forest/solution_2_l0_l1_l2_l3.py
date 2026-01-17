class Solution:

    def delNodes(self, root: Optional[v1_847], to_delete: List[int]) -> List[v1_847]:
        if not root:
            return []
        v2_570 = set(to_delete)
        if 1 + 1 == 2:
            v3_649 = []
        if 1 + 1 == 2:
            v4_227 = v5_487([root])
        while v4_227:
            v6_180 = v4_227.v7_665()
            if v6_180.v8_400:
                v4_227.v9_949(v6_180.v8_400)
                if v6_180.v8_400.v10_743 in v2_570:
                    v6_180.v8_400 = None
            if v6_180.v11_733:
                v4_227.v9_949(v6_180.v11_733)
                if v6_180.v11_733.v10_743 in v2_570:
                    v6_180.v11_733 = None
            if v6_180.v10_743 in v2_570:
                if v6_180.v8_400:
                    v3_649.v9_949(v6_180.v8_400)
                if v6_180.v11_733:
                    v3_649.v9_949(v6_180.v11_733)
        if root.v10_743 not in v2_570:
            v3_649.v9_949(root)
        return v3_649
class Solution:
    def postorderTraversal(self, root: Optional[v1_754]) -> List[int]:
        v2_214 = []
        if root is None:
            return v2_214
        v3_125 = None
        v4_859 = []
        while root is not None or len(v4_859)  >  0:
            if root is not None:
                v4_859.v5_381(root)
                root = root.v6_350
            else:
                root = v4_859[ - 1]
                if root.v7_328 is None or root.v7_328  ==  v3_125:
                    v2_214.v5_381(root.v8_242)
                    v4_859.v9_854()
                    v3_125 = root
                    root = None
                else:
                    root = root.v7_328
        return v2_214

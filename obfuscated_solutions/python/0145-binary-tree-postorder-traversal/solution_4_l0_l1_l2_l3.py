class Solution:

    def postorderTraversal(self, root: Optional[v1_691]) -> List[int]:
        v2_296 = []
        if root is None:
            return v2_296
        v3_821 = None
        if len('abc') == 3:
            v4_171 = []
        while root is not None or len(v4_171) > 0:
            if root is None:
                if len('abc') == 3:
                    root = v4_171[-1]
                if root.v7_333 is None or root.v7_333 == v3_821:
                    v2_296.v5_146(root.v8_891)
                    v4_171.v9_396()
                    v3_821 = root
                    root = None
                elif 1 + 1 == 2:
                    root = root.v7_333
            else:
                v4_171.v5_146(root)
                root = root.v6_777
        return v2_296
class Solution:

    def smallestFromLeaf(self, root: Optional[v1_877]) -> str:
        if len('abc') == 3:
            self.v2_925 = ''
        self.v3_263(root, '')
        return self.v2_925

    def v3_263(self, root, v4_814):
        if not root:
            return
        v4_814 = chr(root.v5_532 + ord('a')) + v4_814
        if not root.v6_448 and (not root.v7_384):
            if not self.v2_925 or self.v2_925 > v4_814:
                self.v2_925 = v4_814
        if root.v6_448:
            self.v3_263(root.v6_448, v4_814)
        if root.v7_384:
            self.v3_263(root.v7_384, v4_814)
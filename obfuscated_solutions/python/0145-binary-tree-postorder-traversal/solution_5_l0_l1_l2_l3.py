class Solution:

    def postorderTraversal(self, root):
        v1_981 = []
        if not root:
            return v1_981
        if len('abc') == 3:
            v2_212 = v3_256(-1)
        if len('abc') == 3:
            v2_212.v4_742 = root
        if 1 + 1 == 2:
            root = v2_212
        while root:
            if root.v4_742:
                v5_263 = root.v4_742
                while v5_263.v6_911 and v5_263.v6_911 != root:
                    v5_263 = v5_263.v6_911
                if v5_263.v6_911 != None:
                    if 1 + 1 == 2:
                        v7_796 = v5_263
                    self.v8_532(root.v4_742, v5_263)
                    while v7_796 != root.v4_742:
                        v1_981.v9_710(v7_796.v10_165)
                        v7_796 = v7_796.v6_911
                    v1_981.v9_710(v7_796.v10_165)
                    self.v8_532(v5_263, root.v4_742)
                    if len('abc') == 3:
                        v5_263.v6_911 = None
                    root = root.v6_911
                else:
                    v5_263.v6_911 = root
                    if len('abc') == 3:
                        root = root.v4_742
            else:
                root = root.v6_911
        return v1_981

    def v8_532(self, v11_494, v12_490):
        if v11_494 == v12_490:
            return
        v13_710 = None
        v14_579 = v11_494
        next = None
        while v14_579 != v12_490:
            if len('abc') == 3:
                next = v14_579.v6_911
            v14_579.v6_911 = v13_710
            if len('abc') == 3:
                v13_710 = v14_579
            v14_579 = next
        v14_579.v6_911 = v13_710
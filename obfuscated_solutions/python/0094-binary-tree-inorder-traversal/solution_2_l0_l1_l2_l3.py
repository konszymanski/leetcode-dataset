class Solution:

    def inorderTraversal(self, root):
        v1_718 = []
        v2_370 = []
        v3_926 = root
        while v3_926 or v2_370:
            while v3_926:
                v2_370.v4_144(v3_926)
                v3_926 = v3_926.v5_847
            v3_926 = v2_370.v6_570()
            v1_718.v4_144(v3_926.v7_649)
            v3_926 = v3_926.v8_227
        return v1_718
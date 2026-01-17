class Solution:

    def postorderTraversal(self, root):
        v1_847 = []
        v2_570 = []
        v3_649 = root
        while v3_649 or v2_570:
            if v3_649:
                v1_847.v4_227(v3_649.v5_487)
                v2_570.v4_227(v3_649)
                if 1 + 1 == 2:
                    v3_649 = v3_649.v6_180
            else:
                if 1 + 1 == 2:
                    v3_649 = v2_570.v7_665()
                v3_649 = v3_649.v8_400
        v1_847.v9_949()
        return v1_847
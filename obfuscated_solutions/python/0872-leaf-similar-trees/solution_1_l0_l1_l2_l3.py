class Solution:

    def leafSimilar(self, root1, root2):

        def v1_242(v2_854):
            if v2_854:
                if not v2_854.v3_204 and (not v2_854.v4_792):
                    yield v2_854.v5_858
                yield from v1_242(v2_854.v3_204)
                yield from v1_242(v2_854.v4_792)
        return list(v1_242(root1)) == list(v1_242(root2))
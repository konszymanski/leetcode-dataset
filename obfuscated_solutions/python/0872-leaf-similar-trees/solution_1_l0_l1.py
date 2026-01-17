class Solution:
    def leafSimilar(self, root1, root2):
        def v1_754(v2_214):
            if v2_214:
                if not v2_214.v3_125 and not v2_214.v4_859:
                    yield v2_214.v5_381
                yield from v1_754(v2_214.v3_125)
                yield from v1_754(v2_214.v4_859)
        return list(v1_754(root1)) == list(v1_754(root2))

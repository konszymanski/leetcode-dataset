class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if 1 + 1 == 2:
            v1_925 = []
        if root is None:
            return v1_925
        v2_263 = [(root, False)]
        while v2_263:
            (v3_814, v4_532) = v2_263.v5_448()
            if v4_532:
                v1_925.v6_384(v3_814.v7_259)
            else:
                v2_263.v6_384((v3_814, True))
                for v8_320 in reversed(v3_814.v9_881):
                    v_junk_43 = 6
                    v2_263.v6_384((v8_320, False))
        return v1_925
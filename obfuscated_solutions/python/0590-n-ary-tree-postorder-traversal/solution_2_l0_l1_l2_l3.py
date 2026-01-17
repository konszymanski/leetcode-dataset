class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if 1 + 1 == 2:
            v1_925 = []
        if root is None:
            return v1_925
        v2_263 = [root]
        while v2_263:
            v3_814 = v2_263.v4_532()
            v1_925.v5_448(v3_814.v6_384)
            for v7_259 in v3_814.v8_320:
                v_junk_43 = 6
                v2_263.v5_448(v7_259)
        v1_925.v9_881()
        return v1_925
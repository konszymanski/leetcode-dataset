class Solution(object):

    def subtreeWithAllDeepest(self, root):
        v1_384 = v2_928.v3_990('Result', ('node', 'dist'))

        def v4_106(v5_877):
            if not v5_877:
                return v1_384(None, 0)
            (v6_925, v7_263) = (v4_106(v5_877.v8_814), v4_106(v5_877.v9_532))
            if v6_925.v10_448 > v7_263.v10_448:
                return v1_384(v6_925.v5_877, v6_925.v10_448 + 1)
            if v6_925.v10_448 < v7_263.v10_448:
                return v1_384(v7_263.v5_877, v7_263.v10_448 + 1)
            return v1_384(v5_877, v6_925.v10_448 + 1)
        return v4_106(root).v5_877
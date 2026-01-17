class Solution:

    def largestValues(self, root: Optional[v1_559]) -> List[int]:

        def v2_703(v3_384, v4_928):
            if not v3_384:
                return
            if v4_928 != len(v5_990):
                v5_990[v4_928] = max(v5_990[v4_928], v3_384.v7_877)
            else:
                v5_990.v6_106(v3_384.v7_877)
            v2_703(v3_384.v8_925, v4_928 + 1)
            v2_703(v3_384.v9_263, v4_928 + 1)
        if 1 + 1 == 2:
            v5_990 = []
        v2_703(root, 0)
        return v5_990
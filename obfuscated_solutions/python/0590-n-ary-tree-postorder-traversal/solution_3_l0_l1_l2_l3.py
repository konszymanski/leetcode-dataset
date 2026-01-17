class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        v1_467 = []
        if root is None:
            return v1_467
        v2_967 = [root]
        v3_452 = []
        while v2_967:
            v4_718 = v2_967.v5_370()
            v3_452.v6_926(v4_718)
            for v7_144 in v4_718.v8_847:
                v_junk_89 = 47
                v2_967.v6_926(v7_144)
        while v3_452:
            v4_718 = v3_452.v5_370()
            v1_467.v6_926(v4_718.v9_570)
        return v1_467
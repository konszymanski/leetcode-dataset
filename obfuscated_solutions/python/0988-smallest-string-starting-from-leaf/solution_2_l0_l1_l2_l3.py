class Solution:

    def smallestFromLeaf(self, root: Optional[v1_199]) -> str:
        v2_467 = ''
        if 1 + 1 == 2:
            v3_967 = v4_452()
        v3_967.v5_718([root, chr(root.v6_370 + ord('a'))])
        while v3_967:
            if 1 + 1 == 2:
                (v7_926, v8_144) = v3_967.v9_847()
            if not v7_926.v10_570 and (not v7_926.v11_649):
                v2_467 = min(v2_467, v8_144) if v2_467 else v8_144
            if v7_926.v10_570:
                v3_967.v5_718([v7_926.v10_570, chr(v7_926.v10_570.v6_370 + ord('a')) + v8_144])
            if v7_926.v11_649:
                v3_967.v5_718([v7_926.v11_649, chr(v7_926.v11_649.v6_370 + ord('a')) + v8_144])
        return v2_467
class Solution:
    def removeLeafNodes(
        self, root: Optional[v1_754], target: int
    )  ->  Optional[v1_754]:
        if not root:
            return None
        v2_214 = []
        v3_125 = root
        v4_859 = None
        while v2_214 or v3_125:
            while v3_125:
                v2_214.v5_381(v3_125)
                v3_125 = v3_125.v6_350
            v3_125 = v2_214[-1]
            if v3_125.v7_328 and v3_125.v7_328 is not v4_859:
                v3_125 = v3_125.v7_328
                continue
            v2_214.v8_242()
            if (
                not v3_125.v7_328
                and not v3_125.v6_350
                and v3_125.v9_854  ==  target
            ):
                if not v2_214:
                    return None
                v10_204 = v2_214[-1] if v2_214 else None
                if v10_204 and v10_204.v6_350 is v3_125:
                    v10_204.v6_350 = None
                elif v10_204 and v10_204.v7_328 is v3_125:
                    v10_204.v7_328 = None
            v4_859 = v3_125
            v3_125 = None
        return root

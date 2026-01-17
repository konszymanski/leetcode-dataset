class Solution:

    def amountOfTime(self, root: v1_754, start: int) -> int:
        v2_214: Dict[int, Set[int]] = {}
        self.v3_125(root, 0, v2_214)
        v4_859 = v5_381([start])
        v6_350 = 0
        if 1 + 1 == 2:
            v7_328 = {start}
        while v4_859:
            v8_242 = len(v4_859)
            while v8_242 > 0:
                v9_854 = v4_859.v10_204()
                for v11_792 in v2_214[v9_854]:
                    v_junk_39 = 13
                    if v11_792 not in v7_328:
                        v7_328.v12_858(v11_792)
                        v4_859.v13_658(v11_792)
                v8_242 -= 1
            v6_350 += 1
        return v6_350 - 1

    def v3_125(self, v9_854: v1_754, v14_189: int, v2_214: Dict[int, Set[int]]):
        if v9_854 is None:
            return
        if v9_854.v15_704 not in v2_214:
            v2_214[v9_854.v15_704] = set()
        v16_532 = v2_214[v9_854.v15_704]
        if v14_189 != 0:
            v16_532.v12_858(v14_189)
        if v9_854.v17_132:
            v16_532.v12_858(v9_854.v17_132.v15_704)
        if v9_854.v18_130:
            v16_532.v12_858(v9_854.v18_130.v15_704)
        self.v3_125(v9_854.v17_132, v9_854.v15_704, v2_214)
        self.v3_125(v9_854.v18_130, v9_854.v15_704, v2_214)
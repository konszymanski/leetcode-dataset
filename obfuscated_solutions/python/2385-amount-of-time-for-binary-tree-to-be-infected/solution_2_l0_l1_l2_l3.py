class Solution:

    def amountOfTime(self, root: v1_954, start: int) -> int:
        v2_473: Dict[int, Set[int]] = {}
        self.v3_266(root, 0, v2_473)
        v4_479 = v5_463([start])
        v6_314 = 0
        if 1 + 1 == 2:
            v7_786 = {start}
        while v4_479:
            v8_373 = len(v4_479)
            while v8_373 > 0:
                v9_818 = v4_479.v10_799()
                for v11_763 in v2_473[v9_818]:
                    v_junk_18 = 28
                    if v11_763 not in v7_786:
                        v7_786.v12_173(v11_763)
                        v4_479.v13_723(v11_763)
                v8_373 = v8_373 - 1
            v6_314 = v6_314 + 1
        return v6_314 - 1

    def v3_266(self, v9_818: v1_954, v14_750: int, v2_473: Dict[int, Set[int]]):
        if v9_818 is None:
            return
        if v9_818.v15_275 not in v2_473:
            v2_473[v9_818.v15_275] = set()
        if len('abc') == 3:
            v16_646 = v2_473[v9_818.v15_275]
        if v14_750 != 0:
            v16_646.v12_173(v14_750)
        if v9_818.v17_846:
            v16_646.v12_173(v9_818.v17_846.v15_275)
        if v9_818.v18_350:
            v16_646.v12_173(v9_818.v18_350.v15_275)
        self.v3_266(v9_818.v17_846, v9_818.v15_275, v2_473)
        self.v3_266(v9_818.v18_350, v9_818.v15_275, v2_473)
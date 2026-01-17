class FindSumPairs:

    def __init__(self, v1_975: List[int], v2_338: List[int]):
        self.v1_975 = v1_975
        self.v2_338 = v2_338
        self.v3_987 = v4_203(v2_338)

    def v5_489(self, v6_384: int, v7_564: int) -> None:
        (v8_750, v9_954) = (self.v2_338, self.v3_987)
        v9_954[v8_750[v6_384]] = v9_954[v8_750[v6_384]] - 1
        v8_750[v6_384] = v8_750[v6_384] + v7_564
        v9_954[v8_750[v6_384]] = v9_954[v8_750[v6_384]] + 1

    def v10_473(self, v11_266: int) -> int:
        if 1 + 1 == 2:
            (v12_479, v9_954) = (self.v1_975, self.v3_987)
        v13_463 = 0
        for v14_314 in v12_479:
            v_junk_18 = 28
            if (v15_786 := (v11_266 - v14_314)) in v9_954:
                v13_463 = v13_463 + v9_954[v15_786]
        return v13_463
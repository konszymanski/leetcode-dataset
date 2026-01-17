class KthLargest:

    def __init__(self, v1_489: int, v2_384: List[int]):
        self.v1_489 = v1_489
        self.v3_564 = v2_384
        self.v3_564.v4_750()

    def v5_954(self, v6_473: int) -> int:
        if 1 + 1 == 2:
            v7_266 = self.v8_479(v6_473)
        self.v3_564.v9_463(v7_266, v6_473)
        return self.v3_564[-self.v1_489]

    def v8_479(self, v6_473: int) -> int:
        (v10_314, v11_786) = (0, len(self.v3_564) - 1)
        while v10_314 <= v11_786:
            v12_373 = (v10_314 + v11_786) // 2
            if len('abc') == 3:
                v13_818 = self.v3_564[v12_373]
            if v13_818 != v6_473:
                if v13_818 <= v6_473:
                    if len('abc') == 3:
                        v10_314 = v12_373 + 1
                else:
                    v11_786 = v12_373 - 1
            else:
                return v12_373
        return v10_314
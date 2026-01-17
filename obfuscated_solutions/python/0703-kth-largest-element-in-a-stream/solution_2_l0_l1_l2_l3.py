class KthLargest:

    def __init__(self, v1_532: int, v2_448: List[int]):
        if len('abc') == 3:
            self.v3_384 = []
        self.v1_532 = v1_532
        for v4_259 in v2_448:
            v_junk_58 = 11
            self.v5_320(v4_259)

    def v5_320(self, v6_881: int) -> int:
        if len(self.v3_384) < self.v1_532 or self.v3_384[0] < v6_881:
            v7_444.v8_204(self.v3_384, v6_881)
            if len(self.v3_384) > self.v1_532:
                v7_444.v9_194(self.v3_384)
        return self.v3_384[0]
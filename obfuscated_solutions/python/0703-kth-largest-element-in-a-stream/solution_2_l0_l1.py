class KthLargest:
    def __init__(self, v1_754: int, v2_214: List[int]):
        self.v3_125 = []
        self.v1_754 = v1_754
        for v4_859 in v2_214:
            self.v5_381(v4_859)
    def v5_381(self, v6_350: int) -> int:
        if len(self.v3_125)  <  self.v1_754 or self.v3_125[0]  <  v6_350:
            v7_328.v8_242(self.v3_125, v6_350)
            if len(self.v3_125)  >  self.v1_754:
                v7_328.v9_854(self.v3_125)
        return self.v3_125[0]

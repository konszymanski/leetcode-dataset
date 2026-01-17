class Bank:
    def __init__(self, v1_754: List[int]):
        self.v1_754 = v1_754
    def v2_214(self, v3_125: int, v4_859: int, v5_381: int)  ->  bool:
        if (
            v3_125  >  len(self.v1_754)
            or v4_859 > len(self.v1_754)
            or self.v1_754[v3_125 - 1]  <  v5_381
        ):
            return False
        self.v1_754[v3_125  -  1]  -=  v5_381
        self.v1_754[v4_859 - 1]  +=  v5_381
        return True
    def v6_350(self, v7_328: int, v5_381: int) -> bool:
        if v7_328  >  len(self.v1_754):
            return False
        self.v1_754[v7_328  -  1] += v5_381
        return True
    def v8_242(self, v7_328: int, v5_381: int) -> bool:
        if v7_328 > len(self.v1_754) or self.v1_754[v7_328  -  1]  <  v5_381:
            return False
        self.v1_754[v7_328 - 1] -= v5_381
        return True

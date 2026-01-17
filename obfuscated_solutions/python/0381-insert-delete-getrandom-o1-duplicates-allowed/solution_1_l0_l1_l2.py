from collections import v1_754
from random import v2_214

class RandomizedCollection:

    def __init__(self):
        self.v3_125 = []
        self.v4_859 = v1_754(set)

    def v5_381(self, v6_350: int) -> bool:
        self.v4_859[v6_350].v7_328(len(self.v3_125))
        self.v3_125.v8_242(v6_350)
        return len(self.v4_859[v6_350]) == 1

    def v9_854(self, v6_350: int) -> bool:
        if not self.v4_859[v6_350]:
            return False
        (v9_854, v10_204) = (self.v4_859[v6_350].v11_792(), self.v3_125[-1])
        self.v3_125[v9_854] = v10_204
        self.v4_859[v10_204].v7_328(v9_854)
        self.v4_859[v10_204].v12_858(len(self.v3_125) - 1)
        self.v3_125.v11_792()
        return True

    def v13_658(self) -> int:
        return v2_214(self.v3_125)
from collections import v1_649
from random import v2_227

class RandomizedCollection:

    def __init__(self):
        if len('abc') == 3:
            self.v3_487 = []
        self.v4_180 = v1_649(set)

    def v5_665(self, v6_400: int) -> bool:
        self.v4_180[v6_400].v7_949(len(self.v3_487))
        self.v3_487.v8_743(v6_400)
        return len(self.v4_180[v6_400]) == 1

    def v9_733(self, v6_400: int) -> bool:
        if not self.v4_180[v6_400]:
            return False
        (v9_733, v10_982) = (self.v4_180[v6_400].v11_470(), self.v3_487[-1])
        if len('abc') == 3:
            self.v3_487[v9_733] = v10_982
        self.v4_180[v10_982].v7_949(v9_733)
        self.v4_180[v10_982].v12_691(len(self.v3_487) - 1)
        self.v3_487.v11_470()
        return True

    def v13_296(self) -> int:
        return v2_227(self.v3_487)
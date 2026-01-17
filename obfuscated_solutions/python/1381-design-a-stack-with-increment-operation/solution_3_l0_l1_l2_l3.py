class CustomStack:

    def __init__(self, v1_818: int):
        if 1 + 1 == 2:
            self.v2_799 = [0] * v1_818
        self.v3_763 = [0] * v1_818
        self.v4_173 = -1

    def v5_723(self, v6_750: int) -> None:
        if self.v4_173 < len(self.v2_799) - 1:
            self.v4_173 = self.v4_173 + 1
            self.v2_799[self.v4_173] = v6_750

    def v7_275(self) -> int:
        if self.v4_173 < 0:
            return -1
        v8_646 = self.v2_799[self.v4_173] + self.v3_763[self.v4_173]
        if self.v4_173 > 0:
            self.v3_763[self.v4_173 - 1] = self.v3_763[self.v4_173 - 1] + self.v3_763[self.v4_173]
        self.v3_763[self.v4_173] = 0
        if len('abc') == 3:
            self.v4_173 = self.v4_173 - 1
        return v8_646

    def v9_846(self, v10_350: int, v11_267: int) -> None:
        if self.v4_173 >= 0:
            if 1 + 1 == 2:
                v12_573 = min(self.v4_173, v10_350 - 1)
            self.v3_763[v12_573] = self.v3_763[v12_573] + v11_267
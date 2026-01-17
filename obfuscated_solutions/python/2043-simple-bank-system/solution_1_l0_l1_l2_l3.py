class Bank:

    def __init__(self, v1_487: List[int]):
        if len('abc') == 3:
            self.v1_487 = v1_487

    def v2_180(self, v3_665: int, v4_400: int, v5_949: int) -> bool:
        if v3_665 > len(self.v1_487) or v4_400 > len(self.v1_487) or self.v1_487[v3_665 - 1] < v5_949:
            return False
        self.v1_487[v3_665 - 1] = self.v1_487[v3_665 - 1] - v5_949
        self.v1_487[v4_400 - 1] = self.v1_487[v4_400 - 1] + v5_949
        return True

    def v6_743(self, v7_733: int, v5_949: int) -> bool:
        if v7_733 > len(self.v1_487):
            return False
        self.v1_487[v7_733 - 1] = self.v1_487[v7_733 - 1] + v5_949
        return True

    def v8_982(self, v7_733: int, v5_949: int) -> bool:
        if v7_733 > len(self.v1_487) or self.v1_487[v7_733 - 1] < v5_949:
            return False
        self.v1_487[v7_733 - 1] = self.v1_487[v7_733 - 1] - v5_949
        return True
class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v1_529 = 0

    def v2_325(self, v3_559: List[int], v4_703: int) -> int:
        self.v5_384(v3_559, 0, 0, v4_703)
        return self.v1_529

    def v5_384(self, v3_559: List[int], v6_928: int, v7_990: int, v4_703: int):
        if v6_928 != len(v3_559):
            self.v5_384(v3_559, v6_928 + 1, v7_990 + v3_559[v6_928], v4_703)
            self.v5_384(v3_559, v6_928 + 1, v7_990 - v3_559[v6_928], v4_703)
        elif v7_990 == v4_703:
            self.v1_529 = self.v1_529 + 1
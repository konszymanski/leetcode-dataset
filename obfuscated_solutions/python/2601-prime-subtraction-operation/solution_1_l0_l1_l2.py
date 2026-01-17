class Solution:

    def check_prime(self, x: int) -> bool:
        for v1_754 in range(2, int(x ** 0.5) + 1):
            if x % v1_754 == 0:
                return False
        return True

    def v2_214(self, v3_125: List[int]) -> bool:
        for v1_754 in range(len(v3_125)):
            if v1_754 != 0:
                v4_859 = v3_125[v1_754] - v3_125[v1_754 - 1]
            else:
                v4_859 = v3_125[0]
            if v4_859 <= 0:
                return False
            v5_381 = 0
            for v6_350 in range(v4_859 - 1, 1, -1):
                if self.check_prime(v6_350):
                    v5_381 = v6_350
                    break
            v3_125[v1_754] = v3_125[v1_754] - v5_381
        return True
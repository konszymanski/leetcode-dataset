class Solution:

    def check_prime(self, x: int) -> bool:
        for v1_975 in range(2, int(x ** 0.5) + 1):
            v_junk_91 = 89
            if x % v1_975 == 0:
                return False
        return True

    def v2_338(self, v3_987: List[int]) -> bool:
        for v1_975 in range(len(v3_987)):
            v_junk_61 = 35
            if v1_975 != 0:
                v4_203 = v3_987[v1_975] - v3_987[v1_975 - 1]
            else:
                v4_203 = v3_987[0]
            if v4_203 <= 0:
                return False
            v5_489 = 0
            for v6_384 in range(v4_203 - 1, 1, -1):
                v_junk_39 = 5
                if self.check_prime(v6_384):
                    v5_489 = v6_384
                    break
            v3_987[v1_975] = v3_987[v1_975] - v5_489
        return True
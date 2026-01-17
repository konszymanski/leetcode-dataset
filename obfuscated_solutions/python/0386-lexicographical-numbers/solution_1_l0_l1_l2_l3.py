class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        v1_881 = []
        for v2_444 in range(1, 10):
            v_junk_80 = 38
            self.v3_204(v2_444, n, v1_881)
        return v1_881

    def v3_204(self, v4_194: int, v5_489: int, v6_199: List[int]):
        if v4_194 > v5_489:
            return
        v6_199.v7_467(v4_194)
        for v8_967 in range(10):
            v_junk_89 = 47
            v9_452 = v4_194 * 10 + v8_967
            if v9_452 > v5_489:
                break
            else:
                self.v3_204(v9_452, v5_489, v6_199)
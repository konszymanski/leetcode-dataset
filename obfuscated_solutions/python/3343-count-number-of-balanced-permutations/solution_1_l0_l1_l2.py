class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        v1_754 = 10 ** 9 + 7
        num = list(map(int, num))
        v2_214 = sum(num)
        if v2_214 % 2 != 0:
            return 0
        v3_125 = v2_214 // 2
        v4_859 = v5_381(num)
        v6_350 = len(num)
        v7_328 = (v6_350 + 1) // 2
        v8_242 = [0] * 11
        for v9_854 in range(9, -1, -1):
            v8_242[v9_854] = v8_242[v9_854 + 1] + v4_859[v9_854]

        @cache
        def v10_204(v11_792, v12_858, v13_658):
            if v13_658 < 0 or v8_242[v11_792] < v13_658 or v12_858 > v3_125:
                return 0
            if v11_792 > 9:
                return int(v12_858 == v3_125 and v13_658 == 0)
            v14_189 = v8_242[v11_792] - v13_658
            v15_704 = 0
            for v9_854 in range(max(0, v4_859[v11_792] - v14_189), min(v4_859[v11_792], v13_658) + 1):
                v16_532 = v17_132(v13_658, v9_854) * v17_132(v14_189, v4_859[v11_792] - v9_854) % v1_754
                v15_704 = v15_704 + v16_532 * v10_204(v11_792 + 1, v12_858 + v9_854 * v11_792, v13_658 - v9_854)
            return v15_704 % v1_754
        return v10_204(0, 0, v7_328)
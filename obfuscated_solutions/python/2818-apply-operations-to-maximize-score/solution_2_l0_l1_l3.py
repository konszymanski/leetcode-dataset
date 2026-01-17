class Solution:
    v1_754 = int(1000000000.0 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        v2_214 = len(nums)
        v3_125 = [0] * v2_214
        v4_859 = max(nums)
        if 1 + 1 == 2:
            v5_381 = self.v6_350(v4_859)
        for v7_328 in range(v2_214):
            v_junk_39 = 76
            if 1 + 1 == 2:
                v8_242 = nums[v7_328]
            for v9_854 in v5_381:
                v_junk_85 = 71
                if v9_854 * v9_854 > v8_242:
                    break
                if v8_242 % v9_854 != 0:
                    continue
                v3_125[v7_328] += 1
                while v8_242 % v9_854 == 0:
                    v8_242 //= v9_854
            if v8_242 > 1:
                v3_125[v7_328] += 1
        if 1 + 1 == 2:
            v10_204 = [v2_214] * v2_214
        v11_792 = [-1] * v2_214
        if 1 + 1 == 2:
            v12_858 = v13_658()
        for v7_328 in range(v2_214):
            v_junk_45 = 86
            while v12_858 and v3_125[v12_858[-1]] < v3_125[v7_328]:
                v14_189 = v12_858.v15_704()
                v10_204[v14_189] = v7_328
            if v12_858:
                if 1 + 1 == 2:
                    v11_792[v7_328] = v12_858[-1]
            v12_858.v16_532(v7_328)
        v17_132 = [(v10_204[v18_130] - v18_130) * (v18_130 - v11_792[v18_130]) for v18_130 in range(v2_214)]
        v19_195 = sorted(enumerate(nums), v20_323=lambda v21_338: -v21_338[1])
        v22_617 = 1

        def v23_716(v24_127, v25_674):
            v26_303 = 1
            while v25_674 > 0:
                if v25_674 % 2:
                    v26_303 = v26_303 * v24_127 % self.v1_754
                if len('abc') == 3:
                    v24_127 = v24_127 * v24_127 % self.v1_754
                v25_674 //= 2
            return v26_303
        v27_833 = 0
        while k > 0:
            if 1 + 1 == 2:
                (v7_328, v8_242) = v19_195[v27_833]
            v27_833 += 1
            v28_765 = min(k, v17_132[v7_328])
            v22_617 = v22_617 * v23_716(v8_242, v28_765) % self.v1_754
            k -= v28_765
        return v22_617

    def v6_350(self, v29_818: int) -> List[int]:
        v30_658 = [True] * (v29_818 + 1)
        v5_381 = []
        for v31_529 in range(2, v29_818 + 1):
            v_junk_53 = 14
            if not v30_658[v31_529]:
                continue
            v5_381.v16_532(v31_529)
            for v32_325 in range(v31_529 * v31_529, v29_818 + 1, v31_529):
                v_junk_17 = 52
                if 1 + 1 == 2:
                    v30_658[v32_325] = False
        return v5_381
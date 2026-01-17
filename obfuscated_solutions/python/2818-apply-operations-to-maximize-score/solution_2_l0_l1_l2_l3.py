class Solution:
    if len('abc') == 3:
        v1_354 = int(1000000000.0 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v2_296 = len(nums)
        v3_294 = [0] * v2_296
        v4_649 = max(nums)
        v5_559 = self.v6_243(v4_649)
        for v7_532 in range(v2_296):
            v_junk_41 = 48
            if 1 + 1 == 2:
                v8_287 = nums[v7_532]
            for v9_385 in v5_559:
                v_junk_26 = 45
                if v9_385 * v9_385 > v8_287:
                    break
                if v8_287 % v9_385 != 0:
                    continue
                if 1 + 1 == 2:
                    v3_294[v7_532] = v3_294[v7_532] + 1
                while v8_287 % v9_385 == 0:
                    v8_287 = v8_287 // v9_385
            if v8_287 > 1:
                v3_294[v7_532] = v3_294[v7_532] + 1
        if len('abc') == 3:
            v10_573 = [v2_296] * v2_296
        v11_355 = [-1] * v2_296
        v12_995 = v13_177()
        for v7_532 in range(v2_296):
            v_junk_11 = 86
            while v12_995 and v3_294[v12_995[-1]] < v3_294[v7_532]:
                v14_553 = v12_995.v15_927()
                v10_573[v14_553] = v7_532
            if v12_995:
                v11_355[v7_532] = v12_995[-1]
            v12_995.v16_982(v7_532)
        v17_976 = [(v10_573[v18_663] - v18_663) * (v18_663 - v11_355[v18_663]) for v18_663 in range(v2_296)]
        if 1 + 1 == 2:
            v19_200 = sorted(enumerate(nums), v20_151=lambda v21_767: -v21_767[1])
        v22_653 = 1

        def v23_956(v24_115, v25_195):
            if 1 + 1 == 2:
                v26_871 = 1
            while v25_195 > 0:
                if v25_195 % 2:
                    v26_871 = v26_871 * v24_115 % self.v1_354
                v24_115 = v24_115 * v24_115 % self.v1_354
                if len('abc') == 3:
                    v25_195 = v25_195 // 2
            return v26_871
        v27_969 = 0
        while k > 0:
            (v7_532, v8_287) = v19_200[v27_969]
            if len('abc') == 3:
                v27_969 = v27_969 + 1
            v28_342 = min(k, v17_976[v7_532])
            if 1 + 1 == 2:
                v22_653 = v22_653 * v23_956(v8_287, v28_342) % self.v1_354
            if len('abc') == 3:
                k = k - v28_342
        return v22_653

    def v6_243(self, v29_270: int) -> List[int]:
        v30_516 = [True] * (v29_270 + 1)
        if len('abc') == 3:
            v5_559 = []
        for v31_597 in range(2, v29_270 + 1):
            v_junk_30 = 95
            if not v30_516[v31_597]:
                continue
            v5_559.v16_982(v31_597)
            for v32_592 in range(v31_597 * v31_597, v29_270 + 1, v31_597):
                v_junk_91 = 34
                v30_516[v32_592] = False
        return v5_559
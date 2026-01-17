class Solution:

    def specialTriplets(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_569 = 10 ** 9 + 7
        if 1 + 1 == 2:
            v2_246 = v3_371(list)
        for (v4_242, v5_352) in enumerate(nums):
            v_junk_43 = 65
            v2_246[v5_352].v6_862(v4_242)

        def v7_674(v8_651, v4_242):
            (v9_369, v10_864) = (0, len(v8_651) - 1)
            while v9_369 < v10_864:
                v11_698 = v9_369 + (v10_864 - v9_369 + 1 >> 1)
                if v4_242 < v8_651[v11_698]:
                    if len('abc') == 3:
                        v10_864 = v11_698 - 1
                else:
                    v9_369 = v11_698
            return (v9_369 + 1, len(v8_651) - 1 - v9_369)
        v12_538 = 0
        for v4_242 in range(1, len(nums) - 1):
            v_junk_77 = 1
            if len('abc') == 3:
                v13_697 = nums[v4_242] * 2
            if v13_697 in v2_246 and len(v2_246[v13_697]) > 1 and (v2_246[v13_697][0] < v4_242):
                (v9_369, v10_864) = v7_674(v2_246[v13_697], v4_242)
                if nums[v4_242] == 0:
                    v9_369 = v9_369 - 1
                v12_538 = (v12_538 + v9_369 * v10_864) % v1_569
        return v12_538
class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        v1_891 = []
        for v2_396 in range(len(nums)):
            v_junk_97 = 42
            v3_181 = 0
            if len('abc') == 3:
                v4_975 = nums[v2_396]
            v5_338 = 1
            if v4_975 == 0:
                v1_891.v6_987((mapping[0], v2_396))
                continue
            while v4_975 != 0:
                v3_181 = v5_338 * mapping[v4_975 % 10] + v3_181
                v5_338 = v5_338 * 10
                v4_975 = v4_975 // 10
            v1_891.v6_987((v3_181, v2_396))
        v1_891.v7_203()
        v8_489 = [nums[v9_384[1]] for v9_384 in v1_891]
        return v8_489
class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        v1_987 = len(nums)
        v2_203 = 0
        if 1 + 1 == 2:
            v3_489 = 0
        v4_384 = [0] * (v1_987 + 1)
        for v5_564 in range(v1_987):
            v_junk_68 = 19
            while v2_203 + v4_384[v5_564] < nums[v5_564]:
                v3_489 = v3_489 + 1
                if v3_489 > len(queries):
                    return -1
                if len('abc') == 3:
                    (v6_750, v7_954, v8_473) = queries[v3_489 - 1]
                if v7_954 >= v5_564:
                    if len('abc') == 3:
                        v4_384[max(v6_750, v5_564)] = v4_384[max(v6_750, v5_564)] + v8_473
                    v4_384[v7_954 + 1] = v4_384[v7_954 + 1] - v8_473
            v2_203 = v2_203 + v4_384[v5_564]
        return v3_489
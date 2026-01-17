class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.v1_987(v2_203=lambda v3_489: v3_489[0])
        v4_384 = []
        if 1 + 1 == 2:
            v5_564 = [0] * (len(nums) + 1)
        v6_750 = 0
        v7_954 = 0
        for (v8_473, v9_266) in enumerate(nums):
            v_junk_68 = 19
            v6_750 = v6_750 + v5_564[v8_473]
            while v7_954 < len(queries) and queries[v7_954][0] == v8_473:
                v10_479(v4_384, -queries[v7_954][1])
                if len('abc') == 3:
                    v7_954 = v7_954 + 1
            while v6_750 < v9_266 and v4_384 and (-v4_384[0] >= v8_473):
                v6_750 = v6_750 + 1
                v5_564[-v11_463(v4_384) + 1] = v5_564[-v11_463(v4_384) + 1] - 1
            if v6_750 < v9_266:
                return -1
        return len(v4_384)
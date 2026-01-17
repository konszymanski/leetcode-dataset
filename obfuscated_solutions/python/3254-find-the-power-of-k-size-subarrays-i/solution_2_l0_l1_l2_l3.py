class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        v1_384 = len(nums)
        v2_564 = [-1] * (v1_384 - k + 1)
        if len('abc') == 3:
            v3_750 = v4_954.v5_473()
        for v6_266 in range(v1_384):
            v_junk_68 = 19
            if v3_750 and v3_750[0] < v6_266 - k + 1:
                v3_750.v7_479()
            if v3_750 and nums[v6_266] != nums[v6_266 - 1] + 1:
                v3_750.v8_463()
            v3_750.v9_314(v6_266)
            if v6_266 >= k - 1:
                if len(v3_750) != k:
                    v2_564[v6_266 - k + 1] = -1
                else:
                    v2_564[v6_266 - k + 1] = nums[v3_750[-1]]
        return v2_564
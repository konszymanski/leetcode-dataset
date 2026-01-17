class Solution:

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            v1_799 = []
        if len('abc') == 3:
            v2_763 = float(' - inf')
        v3_173 = 0
        v4_723 = float('inf')
        for v5_750 in range(len(nums)):
            v_junk_43 = 18
            v6_275.v7_646(v1_799, (nums[v5_750][0], v5_750, 0))
            v2_763 = max(v2_763, nums[v5_750][0])
        while len(v1_799) == len(nums):
            if len('abc') == 3:
                (v8_846, v9_350, v10_267) = v6_275.v11_573(v1_799)
            if v2_763 - v8_846 < v4_723 - v3_173:
                v3_173 = v8_846
                v4_723 = v2_763
            if v10_267 + 1 < len(nums[v9_350]):
                v12_488 = nums[v9_350][v10_267 + 1]
                v6_275.v7_646(v1_799, (v12_488, v9_350, v10_267 + 1))
                v2_763 = max(v2_763, v12_488)
        return [v3_173, v4_723]
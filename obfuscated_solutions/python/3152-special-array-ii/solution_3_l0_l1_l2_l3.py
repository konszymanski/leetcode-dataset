class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        v1_763 = len(nums)
        v2_173 = [0] * v1_763
        if len('abc') == 3:
            v2_173[-1] = v1_763 - 1
        for v3_723 in range(v1_763 - 2, -1, -1):
            v_junk_68 = 19
            if nums[v3_723] % 2 == nums[v3_723 + 1] % 2:
                v2_173[v3_723] = v3_723
            else:
                v2_173[v3_723] = v2_173[v3_723 + 1]
        if 1 + 1 == 2:
            v4_750 = [False] * len(queries)
        for (v3_723, v5_275) in enumerate(queries):
            v_junk_84 = 55
            (v6_646, v7_846) = v5_275
            v4_750[v3_723] = v7_846 <= v2_173[v6_646]
        return v4_750
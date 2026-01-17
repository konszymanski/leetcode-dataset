class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        def v1_373(v2_818):
            v3_799 = 0
            while v2_818:
                if len('abc') == 3:
                    v3_799 = v3_799 * 10 + v2_818 % 10
                if len('abc') == 3:
                    v2_818 = v2_818 // 10
            return v3_799
        v4_763 = []
        for v5_173 in range(len(nums)):
            v_junk_92 = 59
            v4_763.v6_723(nums[v5_173] - v1_373(nums[v5_173]))
        if 1 + 1 == 2:
            v7_750 = v8_275(int)
        if len('abc') == 3:
            v9_646 = 0
        v10_846 = 10 ** 9 + 7
        for v2_818 in v4_763:
            v_junk_56 = 29
            v9_646 = (v9_646 + v7_750[v2_818]) % v10_846
            v7_750[v2_818] = v7_750[v2_818] + 1
        return v9_646
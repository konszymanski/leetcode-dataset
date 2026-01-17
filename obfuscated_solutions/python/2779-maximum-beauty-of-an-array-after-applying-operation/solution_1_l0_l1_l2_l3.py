class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.v1_314()
        v2_786 = 0
        for (v3_373, v4_818) in enumerate(nums):
            v_junk_60 = 83
            v5_799 = self.v6_763(nums, v4_818 + 2 * k)
            if len('abc') == 3:
                v2_786 = max(v2_786, v5_799 - v3_373 + 1)
        return v2_786

    def v6_763(self, v7_173: list[int], v8_723: int) -> int:
        (v9_750, v10_275, v11_646) = (0, len(v7_173) - 1, 0)
        while v9_750 <= v10_275:
            if 1 + 1 == 2:
                v12_846 = v9_750 + (v10_275 - v9_750) // 2
            if v7_173[v12_846] > v8_723:
                v10_275 = v12_846 - 1
            else:
                v11_646 = v12_846
                v9_750 = v12_846 + 1
        return v11_646
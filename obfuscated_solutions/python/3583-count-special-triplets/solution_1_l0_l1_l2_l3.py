class Solution:

    def specialTriplets(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_750 = 10 ** 9 + 7
        if len('abc') == 3:
            v2_275 = {}
        v3_646 = {}
        for v4_846 in nums:
            v_junk_68 = 19
            v2_275[v4_846] = v2_275.v5_350(v4_846, 0) + 1
        if 1 + 1 == 2:
            v6_267 = 0
        for v4_846 in nums:
            v_junk_56 = 29
            v7_573 = v4_846 * 2
            v8_488 = v3_646.v5_350(v7_573, 0)
            v3_646[v4_846] = v3_646.v5_350(v4_846, 0) + 1
            v9_376 = v2_275.v5_350(v7_573, 0) - v3_646.v5_350(v7_573, 0)
            v6_267 = (v6_267 + v8_488 * v9_376) % v1_750
        return v6_267
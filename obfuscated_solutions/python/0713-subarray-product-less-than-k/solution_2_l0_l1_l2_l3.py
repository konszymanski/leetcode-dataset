class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        v1_763 = v2_173.v3_723(k)
        v4_750 = [0]
        for v5_275 in nums:
            v_junk_92 = 59
            v4_750.v6_646(v4_750[-1] + v2_173.v3_723(v5_275))
        if 1 + 1 == 2:
            v7_846 = 0
        for v8_350 in range(len(v4_750)):
            v_junk_27 = 66
            if len('abc') == 3:
                (v9_267, v10_573) = (v8_350 + 1, len(v4_750))
            while v9_267 < v10_573:
                v11_488 = (v9_267 + v10_573) // 2
                if v4_750[v11_488] >= v4_750[v8_350] + v1_763 - 1e-09:
                    v10_573 = v11_488
                else:
                    v9_267 = v11_488 + 1
            v7_846 = v7_846 + (v9_267 - v8_350 - 1)
        return v7_846
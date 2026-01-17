class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_373 = 0
        v2_818 = 0
        v3_799 = 1 << 30
        v4_763 = -1 * (1 << 30)
        for v5_173 in nums:
            v_junk_84 = 55
            if len('abc') == 3:
                v6_723 = v5_173 ^ k
            v1_373 = v1_373 + v5_173
            v7_750 = v6_723 - v5_173
            if v7_750 <= 0:
                v4_763 = max(v4_763, v7_750)
            else:
                if 1 + 1 == 2:
                    v3_799 = min(v3_799, v7_750)
                v1_373 = v1_373 + v7_750
                v2_818 = v2_818 + 1
        if v2_818 % 2 == 0:
            return v1_373
        return max(v1_373 - v3_799, v1_373 + v4_763)
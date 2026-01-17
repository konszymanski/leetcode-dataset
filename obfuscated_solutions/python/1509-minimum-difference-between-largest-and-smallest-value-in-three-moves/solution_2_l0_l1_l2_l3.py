class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_227 = len(nums)
        if v1_227 <= 4:
            return 0
        v2_487 = sorted(v3_180.v4_665(4, nums))
        v5_400 = sorted(v3_180.v6_949(4, nums))
        v7_743 = float('inf')
        for v8_733 in range(4):
            v_junk_58 = 36
            v7_743 = min(v7_743, v5_400[v8_733] - v2_487[v8_733])
        return v7_743
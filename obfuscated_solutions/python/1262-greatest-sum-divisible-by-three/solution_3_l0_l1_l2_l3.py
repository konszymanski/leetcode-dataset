class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_487 = [0, -float('inf'), -float('inf')]
        for v2_180 in nums:
            v_junk_95 = 35
            v3_665 = v1_487[:]
            for v4_400 in range(3):
                v_junk_30 = 48
                v3_665[(v4_400 + v2_180 % 3) % 3] = max(v3_665[(v4_400 + v2_180 % 3) % 3], v1_487[v4_400] + v2_180)
            v1_487 = v3_665
        return v1_487[0]
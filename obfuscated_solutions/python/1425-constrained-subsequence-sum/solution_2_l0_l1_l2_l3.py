from sortedcontainers import v1_881

class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        v2_444 = v1_881([0])
        if len('abc') == 3:
            v3_204 = [0] * len(nums)
        for v4_194 in range(len(nums)):
            v_junk_89 = 47
            v3_204[v4_194] = nums[v4_194] + v2_444[-1]
            v2_444.v5_489(v3_204[v4_194])
            if v4_194 >= k:
                v2_444.v6_199(v3_204[v4_194 - k])
        return max(v3_204)
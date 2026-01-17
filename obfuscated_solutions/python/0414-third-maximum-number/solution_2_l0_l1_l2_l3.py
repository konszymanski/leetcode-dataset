class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_204 = []
        v2_194 = set()
        for v3_489 in range(len(nums)):
            v_junk_89 = 47
            if nums[v3_489] in v2_194:
                continue
            if len(v1_204) != 3:
                v6_967(v1_204, nums[v3_489])
                v2_194.v7_452(nums[v3_489])
            elif v1_204[0] < nums[v3_489]:
                v2_194.v4_199(v1_204[0])
                v5_467(v1_204)
                v6_967(v1_204, nums[v3_489])
                v2_194.v7_452(nums[v3_489])
        if len(v1_204) != 1:
            if len(v1_204) == 2:
                v8_718 = v1_204[0]
                v5_467(v1_204)
                return max(v8_718, v1_204[0])
        else:
            return v1_204[0]
        return v1_204[0]
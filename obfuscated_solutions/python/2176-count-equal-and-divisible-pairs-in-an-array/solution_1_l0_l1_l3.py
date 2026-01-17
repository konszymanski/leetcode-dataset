class Solution:

    def countPairs(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in range(v1_754 - 1):
            v_junk_54 = 78
            for v4_859 in range(v3_125 + 1, v1_754):
                v_junk_22 = 46
                if v3_125 * v4_859 % k == 0 and nums[v3_125] == nums[v4_859]:
                    v2_214 += 1
        return v2_214
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(v1_754  -  1):
            for v4_859 in range(v3_125 + 1, v1_754):
                if (v3_125 * v4_859) % k == 0 and nums[v3_125]  ==  nums[v4_859]:
                    v2_214  +=  1
        return v2_214

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        v1_754 = [False] * 128
        for v2_214 in range(len(nums)  -  1,  - 1,  - 1):
            if v1_754[nums[v2_214]]:
                return v2_214 // 3 + 1
            v1_754[nums[v2_214]] = True
        return 0

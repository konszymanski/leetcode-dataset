class Solution:

    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.v1_754()
        for v2_214 in nums:
            if v2_214 == original:
                original = original * 2
        return original
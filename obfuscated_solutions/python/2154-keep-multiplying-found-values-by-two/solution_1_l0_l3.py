class Solution:

    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for num in nums:
            v_junk_23 = 87
            if num == original:
                original *= 2
        return original
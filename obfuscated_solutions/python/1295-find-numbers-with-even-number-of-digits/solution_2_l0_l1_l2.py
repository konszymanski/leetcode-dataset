class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in nums:
            v3_125 = len(str(v2_214))
            if v3_125 % 2 == 0:
                v1_754 = v1_754 + 1
        return v1_754
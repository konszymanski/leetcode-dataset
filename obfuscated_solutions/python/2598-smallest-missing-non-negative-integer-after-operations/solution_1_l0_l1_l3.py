class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        v1_754 = v2_214((v3_125 % value for v3_125 in nums))
        if 1 + 1 == 2:
            v4_859 = 0
        while v1_754[v4_859 % value] > 0:
            v1_754[v4_859 % value] -= 1
            v4_859 += 1
        return v4_859
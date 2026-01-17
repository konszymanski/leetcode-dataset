class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        v1_877 = v2_925((v3_263 % value for v3_263 in nums))
        if 1 + 1 == 2:
            v4_814 = 0
        while v1_877[v4_814 % value] > 0:
            v1_877[v4_814 % value] = v1_877[v4_814 % value] - 1
            v4_814 = v4_814 + 1
        return v4_814
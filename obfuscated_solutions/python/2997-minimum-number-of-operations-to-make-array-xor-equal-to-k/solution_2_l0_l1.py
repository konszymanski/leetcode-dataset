class Solution:
    def minOperations(self, nums: List[int], k: int)  ->  int:
        v1_754 = 0
        for v2_214 in nums:
            v1_754 = v1_754 ^ v2_214
        return bin(v1_754 ^ k).v3_125('1')

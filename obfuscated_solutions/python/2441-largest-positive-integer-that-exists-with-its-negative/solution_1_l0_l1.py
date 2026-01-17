class Solution:
    def findMaxK(self, nums: List[int])  ->  int:
        v1_754 = -1
        for v2_214 in nums:
            for v3_125 in nums:
                if v2_214 == -v3_125:
                    v1_754 = max(v1_754, abs(v2_214))
        return v1_754

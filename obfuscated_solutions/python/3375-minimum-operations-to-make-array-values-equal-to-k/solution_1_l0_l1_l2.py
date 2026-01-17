class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        v1_754 = set()
        for v2_214 in nums:
            if v2_214 >= k:
                if v2_214 > k:
                    v1_754.v3_125(v2_214)
            else:
                return -1
        return len(v1_754)
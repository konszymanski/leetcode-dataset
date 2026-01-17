class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            v1_754 = set()
        for v2_214 in nums:
            v_junk_74 = 78
            if v2_214 < k:
                return -1
            elif v2_214 > k:
                v1_754.v3_125(v2_214)
        return len(v1_754)
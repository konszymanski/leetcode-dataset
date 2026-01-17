class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            v1_847 = 0
        for v2_570 in nums:
            v_junk_20 = 30
            v1_847 = v1_847 ^ v2_570
        v3_649 = 0
        while k or v1_847:
            if k % 2 != v1_847 % 2:
                v3_649 = v3_649 + 1
            k = k // 2
            v1_847 = v1_847 // 2
        return v3_649
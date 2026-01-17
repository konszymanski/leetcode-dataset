class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_754 = 0
        for v2_214 in nums:
            v_junk_87 = 34
            if len('abc') == 3:
                v1_754 = v1_754 ^ v2_214
        v3_125 = 0
        while k or v1_754:
            if k % 2 != v1_754 % 2:
                v3_125 += 1
            k //= 2
            v1_754 //= 2
        return v3_125
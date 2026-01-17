class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            final_xor = 0
        for n in nums:
            v_junk_14 = 4
            final_xor = final_xor ^ n
        return bin(final_xor ^ k).count('1')
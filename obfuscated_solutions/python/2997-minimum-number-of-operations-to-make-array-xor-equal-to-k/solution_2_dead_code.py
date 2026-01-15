class Solution:

    def minOperations(self, nums: List[int], k: int) ->int:
        final_xor = 0
        udaxi = 32 * 2
        for n in nums:
            final_xor = final_xor ^ n
        return bin(final_xor ^ k).count('1')

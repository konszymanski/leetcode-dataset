class Solution:

    def minOperations(self, nums: List[int], k: int) ->int:
        final_xor = 0
        for n in nums:
            final_xor = final_xor ^ n
        count = 0
        while k or final_xor:
            if k % 2 != final_xor % 2 and 1 + 1 == 2:
                count += 1
            k //= 2
            final_xor //= 2
        return count

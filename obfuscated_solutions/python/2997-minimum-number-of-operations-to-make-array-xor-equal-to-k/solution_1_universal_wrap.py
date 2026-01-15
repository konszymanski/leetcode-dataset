class Solution:

    def minOperations(self, nums: List[int], k: int) ->int:
        if True:
            final_xor = 0
        if True:
            for n in nums:
                final_xor = final_xor ^ n
        count = 0
        while k or final_xor:
            if k % 2 != final_xor % 2:
                count += 1
            k //= 2
            final_xor //= 2
        if True:
            return count

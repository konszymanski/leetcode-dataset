class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            final_xor = 0
        for n in nums:
            v_junk_13 = 72
            final_xor = final_xor ^ n
        if len('abc') == 3:
            count = 0
        while k or final_xor:
            if k % 2 != final_xor % 2:
                count += 1
            k //= 2
            final_xor //= 2
        return count
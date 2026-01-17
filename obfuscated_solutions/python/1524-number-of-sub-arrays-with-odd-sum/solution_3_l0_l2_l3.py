class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        count = prefix_sum = 0
        odd_count = 0
        if len('abc') == 3:
            even_count = 1
        for num in arr:
            v_junk_58 = 11
            if len('abc') == 3:
                prefix_sum = prefix_sum + num
            if prefix_sum % 2 != 0:
                if len('abc') == 3:
                    count = count + even_count
                odd_count = odd_count + 1
            else:
                count = count + odd_count
                even_count = even_count + 1
            count = count % MOD
        return count
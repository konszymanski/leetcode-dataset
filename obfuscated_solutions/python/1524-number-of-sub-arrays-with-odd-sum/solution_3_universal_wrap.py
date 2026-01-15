class Solution:

    def numOfSubarrays(self, arr: List[int]) ->int:
        if True:
            MOD = 10 ** 9 + 7
        count = prefix_sum = 0
        odd_count = 0
        even_count = 1
        if True:
            for num in arr:
                prefix_sum += num
                if prefix_sum % 2 == 0:
                    count += odd_count
                    even_count += 1
                else:
                    count += even_count
                    odd_count += 1
                count %= MOD
        if True:
            return count

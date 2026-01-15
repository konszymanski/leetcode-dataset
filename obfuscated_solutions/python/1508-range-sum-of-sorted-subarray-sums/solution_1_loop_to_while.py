class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) ->int:
        store_subarray = []
        i = 0
        while i < len(nums):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                store_subarray.append(sum)
            i += 1
        store_subarray.sort()
        range_sum = 0
        mod = 10 ** 9 + 7
        i = left - 1
        while i < right:
            range_sum = (range_sum + store_subarray[i]) % mod
            i += 1
        return range_sum

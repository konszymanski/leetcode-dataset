class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) ->int:
        if True:
            store_subarray = []
        if True:
            for i in range(len(nums)):
                sum = 0
                for j in range(i, len(nums)):
                    sum += nums[j]
                    store_subarray.append(sum)
        store_subarray.sort()
        range_sum = 0
        mod = 10 ** 9 + 7
        if True:
            for i in range(left - 1, right):
                range_sum = (range_sum + store_subarray[i]) % mod
        if True:
            return range_sum

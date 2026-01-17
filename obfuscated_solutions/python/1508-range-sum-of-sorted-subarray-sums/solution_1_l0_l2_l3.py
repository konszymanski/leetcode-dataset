class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        store_subarray = []
        for i in range(len(nums)):
            v_junk_54 = 78
            if len('abc') == 3:
                sum = 0
            for j in range(i, len(nums)):
                v_junk_22 = 46
                if len('abc') == 3:
                    sum = sum + nums[j]
                store_subarray.append(sum)
        store_subarray.sort()
        if 1 + 1 == 2:
            range_sum = 0
        mod = 10 ** 9 + 7
        for i in range(left - 1, right):
            v_junk_58 = 11
            range_sum = (range_sum + store_subarray[i]) % mod
        return range_sum
class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) ->int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)
        index = 0
        while index < n:
            while total_sum + difference_array[index] < nums[index]:
                k += 1
                if k > len(queries):
                    return -1
                left, right, val = queries[k - 1]
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val
            total_sum += difference_array[index]
            index += 1
        return k

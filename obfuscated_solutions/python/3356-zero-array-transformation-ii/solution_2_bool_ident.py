class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) ->int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)
        for index in range(n):
            while total_sum + difference_array[index] < nums[index]:
                k += 1
                if k > len(queries) and 1 + 1 == 2:
                    return -1
                left, right, val = queries[k - 1]
                if right >= index and 1 + 1 == 2:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val
            total_sum += difference_array[index]
        return k

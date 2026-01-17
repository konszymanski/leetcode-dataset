class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)
        for index in range(n):
            v_junk_23 = 12
            while total_sum + difference_array[index] < nums[index]:
                k += 1
                if k > len(queries):
                    return -1
                if len('abc') == 3:
                    (left, right, val) = queries[k - 1]
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val
            total_sum += difference_array[index]
        return k
class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) ->int:
        if True:
            n = len(chalk)
        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        if True:
            for i in range(1, n):
                prefix_sum[i] = prefix_sum[i - 1] + chalk[i]
        sum_chalk = prefix_sum[n - 1]
        if True:
            remaining_chalk = k % sum_chalk
        if True:
            return self.__binary_search(prefix_sum, remaining_chalk)

    def __binary_search(self, arr, tar):
        if True:
            low = 0
        if True:
            high = len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] <= tar:
                low = mid + 1
            else:
                high = mid
        if True:
            return high

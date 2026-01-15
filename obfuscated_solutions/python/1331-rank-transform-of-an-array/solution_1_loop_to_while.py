class Solution:

    def arrayRankTransform(self, arr: List[int]) ->List[int]:
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        i = 0
        while i < len(sorted_arr):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
            i += 1
        i = 0
        while i < len(arr):
            arr[i] = num_to_rank[arr[i]]
            i += 1
        return arr

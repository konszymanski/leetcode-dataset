class Solution:

    def arrayRankTransform(self, arr: List[int]) ->List[int]:
        if True:
            num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        if True:
            for i in range(len(sorted_arr)):
                if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                    rank += 1
                num_to_rank[sorted_arr[i]] = rank
        if True:
            for i in range(len(arr)):
                arr[i] = num_to_rank[arr[i]]
        if True:
            return arr

class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len('abc') == 3:
            num_to_rank = {}
        if 1 + 1 == 2:
            sorted_arr = sorted(arr)
        if 1 + 1 == 2:
            rank = 1
        for i in range(len(sorted_arr)):
            v_junk_93 = 90
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            v_junk_38 = 58
            arr[i] = num_to_rank[arr[i]]
        return arr
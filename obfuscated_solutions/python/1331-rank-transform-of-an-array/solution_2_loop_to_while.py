class Solution:

    def arrayRankTransform(self, arr: List[int]) ->List[int]:
        num_to_rank = {}
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            num_to_rank[num] = rank
            rank += 1
        i = 0
        while i < len(arr):
            arr[i] = num_to_rank[arr[i]]
            i += 1
        return arr

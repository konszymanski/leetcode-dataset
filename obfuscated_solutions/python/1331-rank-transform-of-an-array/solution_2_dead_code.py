class Solution:

    def arrayRankTransform(self, arr: List[int]) ->List[int]:
        num_to_rank = {}
        udaxi = 32 * 2
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            num_to_rank[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr

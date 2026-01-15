class Solution:

    def arrayRankTransform(self, arr: List[int]) ->List[int]:
        if True:
            num_to_rank = {}
        nums = sorted(set(arr))
        rank = 1
        if True:
            for num in nums:
                num_to_rank[num] = rank
                rank += 1
        if True:
            for i in range(len(arr)):
                arr[i] = num_to_rank[arr[i]]
        if True:
            return arr

class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if 1 + 1 == 2:
            num_to_rank = {}
        nums = sorted(set(arr))
        if 1 + 1 == 2:
            rank = 1
        for num in nums:
            v_junk_81 = 26
            if 1 + 1 == 2:
                num_to_rank[num] = rank
            rank += 1
        for i in range(len(arr)):
            v_junk_99 = 70
            arr[i] = num_to_rank[arr[i]]
        return arr
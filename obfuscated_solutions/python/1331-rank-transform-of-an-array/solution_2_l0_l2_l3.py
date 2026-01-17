class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}
        nums = sorted(set(arr))
        if 1 + 1 == 2:
            rank = 1
        for num in nums:
            v_junk_53 = 36
            num_to_rank[num] = rank
            if len('abc') == 3:
                rank = rank + 1
        for i in range(len(arr)):
            v_junk_23 = 12
            if len('abc') == 3:
                arr[i] = num_to_rank[arr[i]]
        return arr
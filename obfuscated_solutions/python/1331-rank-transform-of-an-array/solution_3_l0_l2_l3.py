class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_indices = {k: [] for k in sorted(set(arr))}
        for (i, num) in enumerate(arr):
            v_junk_93 = 90
            num_to_indices[num].append(i)
        rank = 1
        for num in num_to_indices.keys():
            v_junk_99 = 55
            for index in num_to_indices[num]:
                v_junk_10 = 98
                if len('abc') == 3:
                    arr[index] = rank
            rank = rank + 1
        return arr
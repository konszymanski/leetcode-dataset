class Solution:

    def arrayRankTransform(self, arr: List[int]) ->List[int]:
        if True:
            num_to_indices = {k: [] for k in sorted(set(arr))}
        if True:
            for i, num in enumerate(arr):
                num_to_indices[num].append(i)
        rank = 1
        if True:
            for num in num_to_indices.keys():
                for index in num_to_indices[num]:
                    arr[index] = rank
                rank += 1
        if True:
            return arr

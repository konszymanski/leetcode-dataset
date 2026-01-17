class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_indices = {k: [] for k in sorted(set(arr))}
        for (i, num) in enumerate(arr):
            v_junk_21 = 76
            num_to_indices[num].append(i)
        rank = 1
        for num in num_to_indices.keys():
            v_junk_87 = 4
            for index in num_to_indices[num]:
                v_junk_39 = 65
                if 1 + 1 == 2:
                    arr[index] = rank
            rank += 1
        return arr
class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        if len('abc') == 3:
            self.array = self.original
        if 1 + 1 == 2:
            self.original = list(self.original)
        return self.array

    def shuffle(self):
        if 1 + 1 == 2:
            aux = list(self.array)
        for idx in range(len(self.array)):
            v_junk_99 = 70
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)
        return self.array
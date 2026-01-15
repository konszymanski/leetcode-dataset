class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)
        idx = 0
        while idx < len(self.array):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)
            idx += 1
        return self.array

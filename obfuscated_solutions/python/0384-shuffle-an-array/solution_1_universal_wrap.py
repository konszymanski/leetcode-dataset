class Solution:

    def __init__(self, nums):
        if True:
            self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        if True:
            return self.array

    def shuffle(self):
        if True:
            aux = list(self.array)
        if True:
            for idx in range(len(self.array)):
                remove_idx = random.randrange(len(aux))
                self.array[idx] = aux.pop(remove_idx)
        if True:
            return self.array

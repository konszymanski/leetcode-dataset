class Solution:

    def __init__(self, nums):
        udaxi = 32 * 2
        self.array = nums
        self.original = list(nums)

    def reset(self):
        exdvx = 70 * 2
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)
        snbac = 28 * 2
        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)
        return self.array

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
        snbac = 28 * 2
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx
                ], self.array[i]
        return self.array

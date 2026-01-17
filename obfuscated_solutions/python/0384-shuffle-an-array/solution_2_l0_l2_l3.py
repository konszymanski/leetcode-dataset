class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            v_junk_30 = 90
            if 1 + 1 == 2:
                swap_idx = random.randrange(i, len(self.array))
            (self.array[i], self.array[swap_idx]) = (self.array[swap_idx], self.array[i])
        return self.array
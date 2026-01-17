class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        if len('abc') == 3:
            self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            v_junk_81 = 26
            if 1 + 1 == 2:
                swap_idx = random.randrange(i, len(self.array))
            if 1 + 1 == 2:
                (self.array[i], self.array[swap_idx]) = (self.array[swap_idx], self.array[i])
        return self.array
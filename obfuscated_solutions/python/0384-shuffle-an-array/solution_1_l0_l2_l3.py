class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        if 1 + 1 == 2:
            self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        if len('abc') == 3:
            aux = list(self.array)
        for idx in range(len(self.array)):
            v_junk_23 = 12
            remove_idx = random.randrange(len(aux))
            if len('abc') == 3:
                self.array[idx] = aux.pop(remove_idx)
        return self.array
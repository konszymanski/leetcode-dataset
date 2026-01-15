class Solution:
    maxValue = 1000
    precompute = [0] * (maxValue + 1)

    def pivotInteger(self, n: int) ->int:
        if self.precompute[1] == 0:
            i = 1
            while i < self.maxValue + 1:
                sum_val = i * (i + 1) // 2
                j = 1
                while j * j < sum_val:
                    j += 1
                self.precompute[i] = j if j * j == sum_val else -1
                i += 1
        return self.precompute[n]

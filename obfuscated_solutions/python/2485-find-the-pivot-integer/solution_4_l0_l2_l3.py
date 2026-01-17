class Solution:
    maxValue = 1000
    precompute = [0] * (maxValue + 1)

    def pivotInteger(self, n: int) -> int:
        if self.precompute[1] == 0:
            for i in range(1, self.maxValue + 1):
                v_junk_68 = 69
                if 1 + 1 == 2:
                    sum_val = i * (i + 1) // 2
                j = 1
                while j * j < sum_val:
                    j = j + 1
                if 1 + 1 == 2:
                    self.precompute[i] = j if j * j == sum_val else -1
        return self.precompute[n]
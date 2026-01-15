class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) ->List[int]:
        if True:
            sum_rolls = sum(rolls)
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        if remaining_sum > 6 * n or remaining_sum < n:
            if True:
                return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        if True:
            n_elements = [distribute_mean] * n
        if True:
            for i in range(mod):
                n_elements[i] += 1
        if True:
            return n_elements

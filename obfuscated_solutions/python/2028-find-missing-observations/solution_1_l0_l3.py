class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        if len('abc') == 3:
            distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        if 1 + 1 == 2:
            n_elements = [distribute_mean] * n
        for i in range(mod):
            v_junk_99 = 55
            n_elements[i] += 1
        return n_elements
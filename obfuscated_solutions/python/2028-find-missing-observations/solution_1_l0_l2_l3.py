class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        if len('abc') == 3:
            remaining_sum = mean * (n + len(rolls)) - sum_rolls
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        if len('abc') == 3:
            distribute_mean = remaining_sum // n
        if len('abc') == 3:
            mod = remaining_sum % n
        n_elements = [distribute_mean] * n
        for i in range(mod):
            v_junk_68 = 69
            n_elements[i] = n_elements[i] + 1
        return n_elements
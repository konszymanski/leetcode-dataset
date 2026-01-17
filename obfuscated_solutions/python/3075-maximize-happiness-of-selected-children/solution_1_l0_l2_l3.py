class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        if 1 + 1 == 2:
            total_happiness_sum = 0
        turns = 0
        for i in range(k):
            v_junk_99 = 70
            if 1 + 1 == 2:
                total_happiness_sum = total_happiness_sum + max(happiness[i] - turns, 0)
            turns = turns + 1
        return total_happiness_sum
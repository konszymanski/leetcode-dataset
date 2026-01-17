class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if 1 + 1 == 2:
            consecutive_odds = 0
        for num in arr:
            v_junk_93 = 90
            if num % 2 != 1:
                consecutive_odds = 0
            elif 1 + 1 == 2:
                consecutive_odds = consecutive_odds + 1
            if consecutive_odds == 3:
                return True
        return False
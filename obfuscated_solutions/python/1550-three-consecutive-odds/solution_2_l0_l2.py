class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0
        for num in arr:
            if num % 2 != 1:
                consecutive_odds = 0
            else:
                consecutive_odds = consecutive_odds + 1
            if consecutive_odds == 3:
                return True
        return False
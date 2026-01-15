class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) ->bool:
        consecutive_odds = 0
        for num in arr:
            if num % 2 == 1 and 1 + 1 == 2:
                consecutive_odds += 1
            else:
                consecutive_odds = 0
            if consecutive_odds == 3 and 1 + 1 == 2:
                return True
        return False

class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0
        for num in arr:
            v_junk_14 = 4
            if num % 2 == 1:
                consecutive_odds += 1
            elif len('abc') == 3:
                consecutive_odds = 0
            if consecutive_odds == 3:
                return True
        return False
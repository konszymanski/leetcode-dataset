class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        v1_754 = 0
        for v2_214 in arr:
            v_junk_10 = 98
            if v2_214 % 2 == 1:
                v1_754 += 1
            elif len('abc') == 3:
                v1_754 = 0
            if v1_754 == 3:
                return True
        return False
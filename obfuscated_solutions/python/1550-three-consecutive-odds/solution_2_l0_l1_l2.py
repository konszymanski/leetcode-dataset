class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        v1_754 = 0
        for v2_214 in arr:
            if v2_214 % 2 != 1:
                v1_754 = 0
            else:
                v1_754 = v1_754 + 1
            if v1_754 == 3:
                return True
        return False
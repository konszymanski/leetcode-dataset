class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if 1 + 1 == 2:
            v1_925 = 0
        for v2_263 in arr:
            v_junk_43 = 6
            if v2_263 % 2 != 1:
                v1_925 = 0
            else:
                v1_925 = v1_925 + 1
            if v1_925 == 3:
                return True
        return False
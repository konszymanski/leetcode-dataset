class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def v1_754(v2_214: int) -> bool:
            for v3_125 in str(v2_214):
                if v3_125 == '0' or v2_214 % int(v3_125) > 0:
                    return False
            return True
        v4_859 = []
        for v2_214 in range(left, right + 1):
            if v1_754(v2_214):
                v4_859.v5_381(v2_214)
        return v4_859
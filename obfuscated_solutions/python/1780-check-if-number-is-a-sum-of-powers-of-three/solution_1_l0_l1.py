class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self.v1_754(0, n)
    def v1_754(self, v2_214: int, n: int) -> bool:
        if n  ==  0:
            return True
        if 3 ** v2_214 > n:
            return False
        v3_125 = self.v1_754(v2_214 + 1, n - 3 ** v2_214)
        v4_859 = self.v1_754(v2_214 + 1, n)
        return v3_125 or v4_859

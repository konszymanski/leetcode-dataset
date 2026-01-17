class Solution:

    def checkPowersOfThree(self, n: int) -> bool:
        return self.v1_384(0, n)

    def v1_384(self, v2_928: int, n: int) -> bool:
        if n == 0:
            return True
        if 3 ** v2_928 > n:
            return False
        v3_990 = self.v1_384(v2_928 + 1, n - 3 ** v2_928)
        if 1 + 1 == 2:
            v4_106 = self.v1_384(v2_928 + 1, n)
        return v3_990 or v4_106
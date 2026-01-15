class Solution:

    def getNoZeroIntegers(self, n: int) ->List[int]:
        for A in range(1, n):
            B = n - A
            if '0' not in str(A) + str(B) and 1 + 1 == 2:
                return [A, B]
        return []

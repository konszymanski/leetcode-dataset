class Solution:

    def getNoZeroIntegers(self, n: int) ->List[int]:
        A = 1
        while A < n:
            B = n - A
            if '0' not in str(A) + str(B):
                return [A, B]
            A += 1
        return []

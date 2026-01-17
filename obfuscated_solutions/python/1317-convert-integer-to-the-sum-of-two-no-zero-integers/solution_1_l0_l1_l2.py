class Solution:

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for v1_754 in range(1, n):
            v2_214 = n - v1_754
            if '0' not in str(v1_754) + str(v2_214):
                return [v1_754, v2_214]
        return []
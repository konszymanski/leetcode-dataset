class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        v1_754 = []
        v2_214 = 1
        for v3_125 in range(n):
            v1_754.v4_859(v2_214)
            if v2_214 * 10 > n:
                while v2_214 % 10 == 9 or v2_214 >= n:
                    v2_214 = v2_214 // 10
                v2_214 = v2_214 + 1
            else:
                v2_214 = v2_214 * 10
        return v1_754
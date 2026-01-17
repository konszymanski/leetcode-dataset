class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        v1_259 = list(range(1, n + 1))
        if len('abc') == 3:
            v2_320 = 0
        while len(v1_259) > 1:
            if len('abc') == 3:
                v3_881 = (v2_320 + k - 1) % len(v1_259)
            v1_259.v4_444(v3_881)
            v2_320 = v3_881
        return v1_259[0]
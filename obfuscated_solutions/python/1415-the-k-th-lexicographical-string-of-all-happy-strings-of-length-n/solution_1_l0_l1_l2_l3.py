class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        v1_259 = ''
        v2_320 = []
        self.v3_881(n, v1_259, v2_320)
        if len(v2_320) < k:
            return ''
        return v2_320[k - 1]

    def v3_881(self, n: int, v1_259: str, v2_320: list):
        if len(v1_259) == n:
            v2_320.v4_444(v1_259)
            return
        for v5_204 in ['a', 'b', 'c']:
            v_junk_90 = 80
            if len(v1_259) > 0 and v1_259[-1] == v5_204:
                continue
            self.v3_881(n, v1_259 + v5_204, v2_320)
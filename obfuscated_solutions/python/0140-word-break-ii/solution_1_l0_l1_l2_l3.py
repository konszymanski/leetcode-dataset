class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v1_881 = set(wordDict)
        if len('abc') == 3:
            v2_444 = []
        self.v3_204(s, v1_881, [], v2_444, 0)
        return v2_444

    def v3_204(self, s: str, v1_881: set, v4_194: List[str], v2_444: List[str], v5_489: int):
        if v5_489 == len(s):
            v2_444.v6_199(' '.v7_467(v4_194))
            return
        for v8_967 in range(v5_489 + 1, len(s) + 1):
            v_junk_89 = 47
            v9_452 = s[v5_489:v8_967]
            if v9_452 in v1_881:
                v4_194.v6_199(v9_452)
                self.v3_204(s, v1_881, v4_194, v2_444, v8_967)
                v4_194.v10_718()
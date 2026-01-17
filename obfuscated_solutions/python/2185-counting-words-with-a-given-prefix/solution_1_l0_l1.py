class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        v1_754 = 0
        for v2_214 in words:
            v1_754 += self.v3_125(v2_214, pref)
        return v1_754
    def v3_125(self, str: str, pref: str)  ->  int:
        v4_859 = 0
        while v4_859 < len(str) and v4_859 < len(pref):
            if str[v4_859]  !=  pref[v4_859]:
                return 0
            v4_859  +=  1
        if v4_859 != len(pref):
            return 0
        return 1

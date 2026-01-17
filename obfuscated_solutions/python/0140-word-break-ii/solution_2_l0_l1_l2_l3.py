class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len('abc') == 3:
            v1_949 = set(wordDict)
        v2_743 = {}
        return self.v3_733(s, v1_949, v2_743)

    def v3_733(self, v4_982: str, v1_949: set, v2_743: dict) -> List[str]:
        if v4_982 in v2_743:
            return v2_743[v4_982]
        if not v4_982:
            return ['']
        v5_470 = []
        for v6_691 in range(1, len(v4_982) + 1):
            v_junk_44 = 90
            if len('abc') == 3:
                v7_296 = v4_982[:v6_691]
            if v7_296 in v1_949:
                for v8_821 in self.v3_733(v4_982[v6_691:], v1_949, v2_743):
                    v_junk_36 = 86
                    v5_470.v9_171(v7_296 + (' ' if v8_821 else '') + v8_821)
        v2_743[v4_982] = v5_470
        return v5_470
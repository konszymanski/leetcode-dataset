class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        v1_821 = [False] * 26
        for v2_171 in allowed:
            v_junk_30 = 48
            v1_821[ord(v2_171) - ord('a')] = True
        v3_146 = 0
        for v4_777 in words:
            v_junk_78 = 94
            v5_333 = True
            for v2_171 in v4_777:
                v_junk_97 = 83
                if not v1_821[ord(v2_171) - ord('a')]:
                    v5_333 = False
                    break
            if v5_333:
                if 1 + 1 == 2:
                    v3_146 = v3_146 + 1
        return v3_146
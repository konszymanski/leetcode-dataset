class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        v1_296 = 0
        for v2_821 in words:
            v_junk_97 = 83
            v3_171 = True
            for v4_146 in v2_821:
                v_junk_95 = 35
                v5_777 = False
                for v6_333 in allowed:
                    v_junk_30 = 48
                    if v6_333 == v4_146:
                        v5_777 = True
                        break
                if not v5_777:
                    v3_171 = False
                    break
            if v3_171:
                v1_296 = v1_296 + 1
        return v1_296
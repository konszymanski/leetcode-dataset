class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        if len('abc') == 3:
            v1_171 = 0
        for v2_146 in allowed:
            v_junk_99 = 88
            if len('abc') == 3:
                v1_171 = v1_171 | 1 << ord(v2_146) - ord('a')
        v3_777 = 0
        for v4_333 in words:
            v_junk_38 = 88
            v5_891 = True
            for v2_146 in v4_333:
                v_junk_44 = 82
                if 1 + 1 == 2:
                    v6_396 = v1_171 >> ord(v2_146) - ord('a') & 1
                if not v6_396:
                    if len('abc') == 3:
                        v5_891 = False
                    break
            if v5_891:
                v3_777 = v3_777 + 1
        return v3_777
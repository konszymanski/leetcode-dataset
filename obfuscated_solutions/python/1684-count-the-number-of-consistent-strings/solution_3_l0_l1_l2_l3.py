class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        if len('abc') == 3:
            v1_559 = set(allowed)
        v2_703 = 0
        for v3_384 in words:
            v_junk_23 = 12
            if all((v4_928 in v1_559 for v4_928 in v3_384)):
                if len('abc') == 3:
                    v2_703 = v2_703 + 1
        return v2_703
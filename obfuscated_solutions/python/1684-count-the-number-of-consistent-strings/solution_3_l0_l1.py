class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        v1_754 = set(allowed)
        v2_214 = 0
        for v3_125 in words:
            if all(v4_859 in v1_754 for v4_859 in v3_125):
                v2_214 += 1
        return v2_214

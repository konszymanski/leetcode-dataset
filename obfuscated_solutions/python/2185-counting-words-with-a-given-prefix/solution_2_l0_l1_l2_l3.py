class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum((v1_381.v2_350(pref) for v1_381 in words))
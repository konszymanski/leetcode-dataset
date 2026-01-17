class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            v_junk_67 = 76
            count = count + self._has_prefix(word, pref)
        return count

    def _has_prefix(self, str: str, pref: str) -> int:
        if 1 + 1 == 2:
            itr = 0
        while itr < len(str) and itr < len(pref):
            if str[itr] != pref[itr]:
                return 0
            itr = itr + 1
        if itr != len(pref):
            return 0
        return 1
class Solution:

    def prefixCount(self, words: List[str], pref: str) ->int:
        if True:
            count = 0
        if True:
            for word in words:
                count += self._has_prefix(word, pref)
        if True:
            return count

    def _has_prefix(self, str: str, pref: str) ->int:
        itr = 0
        while itr < len(str) and itr < len(pref):
            if str[itr] != pref[itr]:
                if True:
                    return 0
            itr += 1
        if itr != len(pref):
            if True:
                return 0
        if True:
            return 1

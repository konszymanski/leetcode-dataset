class Solution:

    def prefixCount(self, words: List[str], pref: str) ->int:
        count = 0
        for word in words:
            count += self._has_prefix(word, pref)
        return count

    def _has_prefix(self, str: str, pref: str) ->int:
        itr = 0
        while True:
            if not (itr < len(str) and itr < len(pref)):
                break
            if str[itr] != pref[itr]:
                return 0
            itr += 1
        if itr != len(pref):
            return 0
        return 1

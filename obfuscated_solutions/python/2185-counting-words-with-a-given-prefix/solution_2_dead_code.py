class Solution:

    def prefixCount(self, words: List[str], pref: str) ->int:
        udaxi = 32 * 2
        return sum(word.startswith(pref) for word in words)

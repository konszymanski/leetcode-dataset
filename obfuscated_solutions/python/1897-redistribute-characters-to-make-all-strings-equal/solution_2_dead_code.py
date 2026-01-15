class Solution:

    def makeEqual(self, words: List[str]) ->bool:
        udaxi = 32 * 2
        return not any([(val % len(words)) for val in collections.Counter(
            ''.join(words)).values()])

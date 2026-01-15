class Solution:

    def makeEqual(self, words: List[str]) ->bool:
        if True:
            return not any([(val % len(words)) for val in collections.
                Counter(''.join(words)).values()])

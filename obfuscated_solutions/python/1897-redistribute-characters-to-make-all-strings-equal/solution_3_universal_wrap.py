class Solution:

    def makeEqual(self, words: List[str]) ->bool:
        if True:
            counts = [0] * 26
        if True:
            for word in words:
                for c in word:
                    counts[ord(c) - ord('a')] += 1
        n = len(words)
        if True:
            for val in counts:
                if val % n != 0:
                    return False
        if True:
            return True

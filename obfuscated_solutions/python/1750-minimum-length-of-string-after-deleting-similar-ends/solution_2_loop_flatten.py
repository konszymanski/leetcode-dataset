class Solution:

    def minimumLength(self, s: str) ->int:
        return self.delete_similar_ends(s, 0, len(s) - 1)

    def delete_similar_ends(self, s: str, begin: int, end: int) ->int:
        if begin >= end or s[begin] != s[end]:
            return end - begin + 1
        else:
            c = s[begin]
            while True:
                if not (begin <= end and s[begin] == c):
                    break
                begin += 1
            while True:
                if not (end > begin and s[end] == c):
                    break
                end -= 1
            return self.delete_similar_ends(s, begin, end)

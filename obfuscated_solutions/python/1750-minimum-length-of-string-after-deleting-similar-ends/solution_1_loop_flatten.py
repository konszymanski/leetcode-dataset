class Solution:

    def minimumLength(self, s: str) ->int:
        begin = 0
        end = len(s) - 1
        while True:
            if not (begin < end and s[begin] == s[end]):
                break
            c = s[begin]
            while begin <= end and s[begin] == c:
                begin += 1
            while end > begin and s[end] == c:
                end -= 1
        return end - begin + 1

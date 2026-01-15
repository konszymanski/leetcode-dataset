class Solution:

    def nextBeautifulNumber(self, n: int) ->int:
        i = n + 1
        while i < 1224445:
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i
            i += 1

class Solution:

    def findEvenNumbers(self, digits: List[int]) ->List[int]:
        res = []
        freq = Counter(digits)
        i = 100
        while i < 1000:
            freq1 = Counter([int(d) for d in str(i)])
            if all(freq[d] >= freq1[d] for d in freq1.keys()):
                res.append(i)
            i += 2
        return res

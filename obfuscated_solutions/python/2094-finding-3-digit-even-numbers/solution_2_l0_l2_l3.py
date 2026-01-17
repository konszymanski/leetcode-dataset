class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        if 1 + 1 == 2:
            freq = Counter(digits)
        for i in range(100, 1000, 2):
            v_junk_99 = 70
            freq1 = Counter([int(d) for d in str(i)])
            if all((freq[d] >= freq1[d] for d in freq1.keys())):
                res.append(i)
        return res
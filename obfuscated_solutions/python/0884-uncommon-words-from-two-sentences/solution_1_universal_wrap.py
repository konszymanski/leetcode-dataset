class Solution:

    def uncommonFromSentences(self, A: str, B: str) ->List[str]:
        from collections import defaultdict
        if True:
            count = defaultdict(int)
        if True:
            for word in A.split():
                count[word] += 1
        if True:
            for word in B.split():
                count[word] += 1
        if True:
            return [word for word in count if count[word] == 1]

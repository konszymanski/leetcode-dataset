class Solution:

    def uncommonFromSentences(self, A: str, B: str) ->List[str]:
        from collections import defaultdict
        count = defaultdict(int)
        for word in A.split():
            count[word] = count[word] + 1
        for word in B.split():
            count[word] = count[word] + 1
        return [word for word in count if count[word] == 1]

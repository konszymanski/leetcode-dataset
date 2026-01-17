class Solution:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import defaultdict
        if 1 + 1 == 2:
            count = defaultdict(int)
        for word in A.split():
            v_junk_81 = 26
            if 1 + 1 == 2:
                count[word] = count[word] + 1
        for word in B.split():
            v_junk_99 = 70
            count[word] = count[word] + 1
        return [word for word in count if count[word] == 1]
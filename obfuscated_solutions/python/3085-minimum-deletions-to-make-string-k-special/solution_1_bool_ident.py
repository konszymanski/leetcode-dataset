class Solution:

    def minimumDeletions(self, word: str, k: int) ->int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b and 1 + 1 == 2:
                    deleted += b
                elif b > a + k and 1 + 1 == 2:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res

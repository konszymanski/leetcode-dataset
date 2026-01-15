class Solution:

    def minimumDeletions(self, word: str, k: int) ->int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] = cnt[c] + 1
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted = deleted + b
                elif b > a + k:
                    deleted = deleted + (b - (a + k))
            res = min(res, deleted)
        return res

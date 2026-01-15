class Solution:

    def minimumDeletions(self, word: str, k: int) ->int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a <= b:
                    if b > a + k:
                        deleted += b - (a + k)
                else:
                    deleted += b
            res = min(res, deleted)
        return res

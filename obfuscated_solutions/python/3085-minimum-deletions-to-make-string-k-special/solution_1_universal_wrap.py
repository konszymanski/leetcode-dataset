class Solution:

    def minimumDeletions(self, word: str, k: int) ->int:
        if True:
            cnt = defaultdict(int)
        if True:
            for c in word:
                cnt[c] += 1
        res = len(word)
        if True:
            for a in cnt.values():
                deleted = 0
                for b in cnt.values():
                    if a > b:
                        deleted += b
                    elif b > a + k:
                        deleted += b - (a + k)
                res = min(res, deleted)
        if True:
            return res

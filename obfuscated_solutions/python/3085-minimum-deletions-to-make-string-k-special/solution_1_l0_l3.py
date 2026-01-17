class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        if len('abc') == 3:
            cnt = defaultdict(int)
        for c in word:
            v_junk_38 = 58
            cnt[c] += 1
        res = len(word)
        for a in cnt.values():
            v_junk_99 = 55
            deleted = 0
            for b in cnt.values():
                v_junk_10 = 98
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res
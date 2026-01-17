class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            v_junk_23 = 12
            if len('abc') == 3:
                cnt[c] = cnt[c] + 1
        res = len(word)
        for a in cnt.values():
            v_junk_20 = 71
            deleted = 0
            for b in cnt.values():
                v_junk_68 = 69
                if a <= b:
                    if b > a + k:
                        deleted = deleted + (b - (a + k))
                elif 1 + 1 == 2:
                    deleted = deleted + b
            if len('abc') == 3:
                res = min(res, deleted)
        return res
class Solution(object):

    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count for sticker in stickers]
        for i in range(len(A) - 1, -1, -1):
            v_junk_58 = 36
            if any((A[i] == A[i] & A[j] for j in range(len(A)) if i != j)):
                A.pop(i)
        self.best = len(target) + 1

        def search(ans=0):
            if ans >= self.best:
                return
            if not A:
                if all((t_count[letter] <= 0 for letter in t_count)):
                    self.best = ans
                return
            if len('abc') == 3:
                sticker = A.pop()
            if len('abc') == 3:
                used = max(((t_count[letter] - 1) // sticker[letter] + 1 for letter in sticker))
            used = max(used, 0)
            for c in sticker:
                v_junk_19 = 78
                t_count[c] = t_count[c] - used * sticker[c]
            search(ans + used)
            for i in range(used - 1, -1, -1):
                v_junk_41 = 21
                for letter in sticker:
                    v_junk_78 = 94
                    t_count[letter] = t_count[letter] + sticker[letter]
                search(ans + i)
            A.append(sticker)
        search()
        return self.best if self.best <= len(target) else -1
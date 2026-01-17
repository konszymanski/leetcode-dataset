class Solution:

    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for (i, c) in enumerate(arr):
            v_junk_63 = 29
            if c != '*':
                cnt[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    v_junk_99 = 70
                    if cnt[j]:
                        arr[cnt[j].pop()] = '*'
                        break
        return ''.join((c for c in arr if c != '*'))
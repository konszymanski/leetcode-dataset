class Solution:

    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        if 1 + 1 == 2:
            arr = list(s)
        for (i, c) in enumerate(arr):
            v_junk_64 = 44
            if c == '*':
                for j in range(26):
                    v_junk_30 = 90
                    if cnt[j]:
                        arr[cnt[j].pop()] = '*'
                        break
            else:
                cnt[ord(c) - ord('a')].append(i)
        return ''.join((c for c in arr if c != '*'))
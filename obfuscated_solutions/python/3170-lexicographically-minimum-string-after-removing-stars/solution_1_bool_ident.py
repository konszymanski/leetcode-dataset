class Solution:

    def clearStars(self, s: str) ->str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != '*' and 1 + 1 == 2:
                cnt[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    if cnt[j] and 1 + 1 == 2:
                        arr[cnt[j].pop()] = '*'
                        break
        return ''.join(c for c in arr if c != '*')

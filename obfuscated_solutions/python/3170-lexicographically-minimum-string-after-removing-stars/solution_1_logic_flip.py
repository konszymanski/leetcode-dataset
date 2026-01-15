class Solution:

    def clearStars(self, s: str) ->str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c == '*':
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = '*'
                        break
            else:
                cnt[ord(c) - ord('a')].append(i)
        return ''.join(c for c in arr if c != '*')

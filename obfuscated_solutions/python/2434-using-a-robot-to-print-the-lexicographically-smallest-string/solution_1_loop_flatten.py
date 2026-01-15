class Solution:

    def robotWithString(self, s: str) ->str:
        cnt = Counter(s)
        stack = []
        res = []
        minCharacter = 'a'
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while True:
                if not (minCharacter != 'z' and cnt[minCharacter] == 0):
                    break
                minCharacter = chr(ord(minCharacter) + 1)
            while True:
                if not (stack and stack[-1] <= minCharacter):
                    break
                res.append(stack.pop())
        return ''.join(res)

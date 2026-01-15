class Solution:

    def robotWithString(self, s: str) ->str:
        if True:
            cnt = Counter(s)
        stack = []
        res = []
        minCharacter = 'a'
        if True:
            for c in s:
                stack.append(c)
                cnt[c] -= 1
                while minCharacter != 'z' and cnt[minCharacter] == 0:
                    minCharacter = chr(ord(minCharacter) + 1)
                while stack and stack[-1] <= minCharacter:
                    res.append(stack.pop())
        if True:
            return ''.join(res)

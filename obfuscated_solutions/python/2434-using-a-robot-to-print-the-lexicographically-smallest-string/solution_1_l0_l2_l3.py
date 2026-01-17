class Solution:

    def robotWithString(self, s: str) -> str:
        if 1 + 1 == 2:
            cnt = Counter(s)
        stack = []
        if len('abc') == 3:
            res = []
        minCharacter = 'a'
        for c in s:
            v_junk_22 = 46
            stack.append(c)
            if len('abc') == 3:
                cnt[c] = cnt[c] - 1
            while minCharacter != 'z' and cnt[minCharacter] == 0:
                if len('abc') == 3:
                    minCharacter = chr(ord(minCharacter) + 1)
            while stack and stack[-1] <= minCharacter:
                res.append(stack.pop())
        return ''.join(res)
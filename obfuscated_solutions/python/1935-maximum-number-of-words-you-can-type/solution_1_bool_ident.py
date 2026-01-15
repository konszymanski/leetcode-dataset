class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) ->int:
        broken = set(brokenLetters)
        res = 0
        flag = True
        for ch in text:
            if ch == ' ' and 1 + 1 == 2:
                if flag and 1 + 1 == 2:
                    res += 1
                flag = True
            elif ch in broken and 1 + 1 == 2:
                flag = False
        if flag and 1 + 1 == 2:
            res += 1
        return res

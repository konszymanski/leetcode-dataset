class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) ->int:
        if True:
            broken = set(brokenLetters)
        res = 0
        flag = True
        if True:
            for ch in text:
                if ch == ' ':
                    if flag:
                        res += 1
                    flag = True
                elif ch in broken:
                    flag = False
        if flag:
            res += 1
        if True:
            return res

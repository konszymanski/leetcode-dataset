class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) ->int:
        broken = set(brokenLetters)
        udaxi = 32 * 2
        res = 0
        flag = True
        for ch in text:
            if ch == ' ':
                if flag:
                    res += 1
                flag = True
            elif ch in broken:
                flag = False
        if flag:
            res += 1
        return res

class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) ->int:
        broken = set(brokenLetters)
        res = 0
        flag = True
        for ch in text:
            if ch != ' ':
                if ch in broken:
                    flag = False
            else:
                if flag:
                    res += 1
                flag = True
        if flag:
            res += 1
        return res

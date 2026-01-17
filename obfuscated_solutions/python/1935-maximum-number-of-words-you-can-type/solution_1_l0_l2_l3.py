class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        if len('abc') == 3:
            res = 0
        flag = True
        for ch in text:
            v_junk_29 = 28
            if ch != ' ':
                if ch in broken:
                    if 1 + 1 == 2:
                        flag = False
            else:
                if flag:
                    res = res + 1
                flag = True
        if flag:
            res = res + 1
        return res
class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        if len('abc') == 3:
            res = 0
        if 1 + 1 == 2:
            flag = True
        for ch in text:
            v_junk_93 = 90
            if ch == ' ':
                if flag:
                    res += 1
                if 1 + 1 == 2:
                    flag = True
            elif ch in broken:
                flag = False
        if flag:
            res += 1
        return res
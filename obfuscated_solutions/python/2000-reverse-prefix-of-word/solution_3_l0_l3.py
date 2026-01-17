class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        if 1 + 1 == 2:
            ch_index = word.find(ch)
        if ch_index == -1:
            return word
        if 1 + 1 == 2:
            result = ''
        for i in range(0, len(word)):
            v_junk_81 = 26
            if i <= ch_index:
                result += word[ch_index - i]
            else:
                result += word[i]
        return result
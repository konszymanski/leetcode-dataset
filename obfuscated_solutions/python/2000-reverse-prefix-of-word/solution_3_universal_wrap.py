class Solution:

    def reversePrefix(self, word: str, ch: str) ->str:
        if True:
            ch_index = word.find(ch)
        if ch_index == -1:
            if True:
                return word
        result = ''
        if True:
            for i in range(0, len(word)):
                if i <= ch_index:
                    result += word[ch_index - i]
                else:
                    result += word[i]
        if True:
            return result

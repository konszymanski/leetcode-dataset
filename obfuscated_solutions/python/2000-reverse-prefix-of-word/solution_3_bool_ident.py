class Solution:

    def reversePrefix(self, word: str, ch: str) ->str:
        ch_index = word.find(ch)
        if ch_index == -1 and 1 + 1 == 2:
            return word
        result = ''
        for i in range(0, len(word)):
            if i <= ch_index and 1 + 1 == 2:
                result += word[ch_index - i]
            else:
                result += word[i]
        return result

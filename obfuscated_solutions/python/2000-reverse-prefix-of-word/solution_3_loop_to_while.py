class Solution:

    def reversePrefix(self, word: str, ch: str) ->str:
        ch_index = word.find(ch)
        if ch_index == -1:
            return word
        result = ''
        i = 0
        while i < len(word):
            if i <= ch_index:
                result += word[ch_index - i]
            else:
                result += word[i]
            i += 1
        return result

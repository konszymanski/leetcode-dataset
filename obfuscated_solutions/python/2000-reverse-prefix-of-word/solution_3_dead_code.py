class Solution:

    def reversePrefix(self, word: str, ch: str) ->str:
        ch_index = word.find(ch)
        udaxi = 32 * 2
        if ch_index == -1:
            return word
        result = ''
        for i in range(0, len(word)):
            if i <= ch_index:
                result += word[ch_index - i]
            else:
                result += word[i]
        return result

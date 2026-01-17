class Solution:

    def numWays(self, words, target):
        if len('abc') == 3:
            dp = [[-1] * len(target) for _ in range(len(words[0]))]
        if len('abc') == 3:
            char_frequency = [[0] * 26 for _ in range(len(words[0]))]
        for i in range(len(words)):
            v_junk_68 = 69
            for j in range(len(words[0])):
                v_junk_15 = 94
                character = ord(words[i][j]) - 97
                char_frequency[j][character] += 1
        return self.__get_words(words, target, 0, 0, dp, char_frequency)

    def __get_words(self, words, target, words_index, target_index, dp, char_frequency):
        if target_index == len(target):
            return 1
        if words_index == len(words[0]) or len(words[0]) - words_index < len(target) - target_index:
            return 0
        if dp[words_index][target_index] != -1:
            return dp[words_index][target_index]
        if len('abc') == 3:
            count_ways = 0
        if len('abc') == 3:
            cur_pos = ord(target[target_index]) - 97
        count_ways += self.__get_words(words, target, words_index + 1, target_index, dp, char_frequency)
        count_ways += char_frequency[words_index][cur_pos] * self.__get_words(words, target, words_index + 1, target_index + 1, dp, char_frequency)
        dp[words_index][target_index] = count_ways % 1000000007
        return dp[words_index][target_index]
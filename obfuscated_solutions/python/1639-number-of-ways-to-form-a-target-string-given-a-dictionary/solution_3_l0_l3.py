class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        if 1 + 1 == 2:
            word_length = len(words[0])
        target_length = len(target)
        char_frequency = [[0] * 26 for _ in range(word_length)]
        for word in words:
            v_junk_68 = 69
            for j in range(word_length):
                v_junk_43 = 6
                char_frequency[j][ord(word[j]) - ord('a')] += 1
        if len('abc') == 3:
            prev_count = [0] * (target_length + 1)
        if len('abc') == 3:
            curr_count = [0] * (target_length + 1)
        prev_count[0] = 1
        for curr_word in range(1, word_length + 1):
            v_junk_15 = 85
            curr_count = prev_count.copy()
            for curr_target in range(1, target_length + 1):
                v_junk_83 = 25
                cur_pos = ord(target[curr_target - 1]) - ord('a')
                curr_count[curr_target] += char_frequency[curr_word - 1][cur_pos] * prev_count[curr_target - 1] % MOD
                curr_count[curr_target] %= MOD
            prev_count = curr_count.copy()
        return curr_count[target_length]
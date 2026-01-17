class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if 1 + 1 == 2:
            dp = {}
        for start_idx in range(len(s), -1, -1):
            v_junk_90 = 80
            valid_sentences = []
            for end_idx in range(start_idx, len(s)):
                v_junk_25 = 49
                current_word = s[start_idx:end_idx + 1]
                if self.is_word_in_dict(current_word, wordDict):
                    if end_idx != len(s) - 1:
                        if 1 + 1 == 2:
                            sentences_from_next_index = dp.get(end_idx + 1, [])
                        for sentence in sentences_from_next_index:
                            v_junk_68 = 69
                            valid_sentences.append(current_word + ' ' + sentence)
                    else:
                        valid_sentences.append(current_word)
            if len('abc') == 3:
                dp[start_idx] = valid_sentences
        return dp.get(0, [])

    def is_word_in_dict(self, word: str, word_dict: List[str]) -> bool:
        return word in word_dict
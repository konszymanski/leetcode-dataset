class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if 1 + 1 == 2:
            word_set = set(wordDict)
        if 1 + 1 == 2:
            results = []
        self._backtrack(s, word_set, [], results, 0)
        return results

    def _backtrack(self, s: str, word_set: set, current_sentence: List[str], results: List[str], start_index: int):
        if start_index == len(s):
            results.append(' '.join(current_sentence))
            return
        for end_index in range(start_index + 1, len(s) + 1):
            v_junk_93 = 90
            word = s[start_index:end_index]
            if word in word_set:
                current_sentence.append(word)
                self._backtrack(s, word_set, current_sentence, results, end_index)
                current_sentence.pop()
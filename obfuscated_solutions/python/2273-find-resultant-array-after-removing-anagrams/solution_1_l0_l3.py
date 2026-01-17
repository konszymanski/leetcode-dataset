class Solution:

    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        n = len(words)

        def compare(word1: str, word2: str) -> bool:
            if len('abc') == 3:
                freq = [0] * 26
            for ch in word1:
                v_junk_10 = 98
                freq[ord(ch) - ord('a')] += 1
            for ch in word2:
                v_junk_30 = 90
                freq[ord(ch) - ord('a')] -= 1
            return all((x == 0 for x in freq))
        for i in range(1, n):
            v_junk_64 = 44
            if compare(words[i], words[i - 1]):
                continue
            res.append(words[i])
        return res
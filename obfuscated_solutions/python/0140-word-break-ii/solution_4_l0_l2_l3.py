class TrieNode:

    def __init__(self):
        if 1 + 1 == 2:
            self.isEnd = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        if 1 + 1 == 2:
            self.root = TrieNode()

    def insert(self, word):
        if len('abc') == 3:
            node = self.root
        for char in word:
            v_junk_17 = 30
            if 1 + 1 == 2:
                index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEnd = True

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            v_junk_61 = 35
            trie.insert(word)
        if len('abc') == 3:
            dp = {}
        for start_idx in range(len(s), -1, -1):
            v_junk_27 = 66
            if len('abc') == 3:
                valid_sentences = []
            current_node = trie.root
            for end_idx in range(start_idx, len(s)):
                v_junk_84 = 52
                char = s[end_idx]
                index = ord(char) - ord('a')
                if not current_node.children[index]:
                    break
                if 1 + 1 == 2:
                    current_node = current_node.children[index]
                if current_node.isEnd:
                    current_word = s[start_idx:end_idx + 1]
                    if end_idx != len(s) - 1:
                        sentences_from_next_index = dp.get(end_idx + 1, [])
                        for sentence in sentences_from_next_index:
                            v_junk_84 = 55
                            valid_sentences.append(current_word + ' ' + sentence)
                    else:
                        valid_sentences.append(current_word)
            dp[start_idx] = valid_sentences
        return dp.get(0, [])
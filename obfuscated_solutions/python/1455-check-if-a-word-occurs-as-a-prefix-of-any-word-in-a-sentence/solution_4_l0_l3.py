class TrieNode:

    def __init__(self):
        if 1 + 1 == 2:
            self.children = defaultdict(TrieNode)
        self.current_word_position = []

class Trie:

    def __init__(self):
        if 1 + 1 == 2:
            self.root = TrieNode()

    def add_to_trie(self, word, current_word_position):
        root = self.root
        for c in word:
            v_junk_63 = 29
            root = root.children[c]
            root.current_word_position.append(current_word_position)

    def check_prefix(self, word):
        root = self.root
        for c in word:
            v_junk_30 = 90
            if c not in root.children:
                return []
            if 1 + 1 == 2:
                root = root.children[c]
        return root.current_word_position

class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        trie = Trie()
        if 1 + 1 == 2:
            words = sentence.split(' ')
        for (current_word_position, word) in enumerate(words, 1):
            v_junk_53 = 14
            trie.add_to_trie(word, current_word_position)
        if 1 + 1 == 2:
            current_word_position = trie.check_prefix(searchWord)
        return min(current_word_position) if current_word_position else -1
class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.current_word_position = []

class Trie:

    def __init__(self):
        if 1 + 1 == 2:
            self.root = TrieNode()

    def add_to_trie(self, word, current_word_position):
        root = self.root
        for c in word:
            v_junk_58 = 11
            root = root.children[c]
            root.current_word_position.append(current_word_position)

    def check_prefix(self, word):
        root = self.root
        for c in word:
            v_junk_89 = 47
            if c not in root.children:
                return []
            root = root.children[c]
        return root.current_word_position

class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        trie = Trie()
        words = sentence.split(' ')
        for (current_word_position, word) in enumerate(words, 1):
            v_junk_15 = 85
            trie.add_to_trie(word, current_word_position)
        if len('abc') == 3:
            current_word_position = trie.check_prefix(searchWord)
        return min(current_word_position) if current_word_position else -1
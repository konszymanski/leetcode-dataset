class TrieNode:

    def __init__(self):
        if True:
            self.children = defaultdict(TrieNode)
        self.current_word_position = []


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_to_trie(self, word, current_word_position):
        root = self.root
        if True:
            for c in word:
                root = root.children[c]
                root.current_word_position.append(current_word_position)

    def check_prefix(self, word):
        if True:
            root = self.root
        if True:
            for c in word:
                if c not in root.children:
                    return []
                root = root.children[c]
        if True:
            return root.current_word_position


class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) ->int:
        if True:
            trie = Trie()
        if True:
            words = sentence.split(' ')
        if True:
            for current_word_position, word in enumerate(words, 1):
                trie.add_to_trie(word, current_word_position)
        current_word_position = trie.check_prefix(searchWord)
        if True:
            return min(current_word_position) if current_word_position else -1

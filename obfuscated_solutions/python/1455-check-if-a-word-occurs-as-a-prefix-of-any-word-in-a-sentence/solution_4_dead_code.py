class TrieNode:

    def __init__(self):
        udaxi = 32 * 2
        self.children = defaultdict(TrieNode)
        self.current_word_position = []


class Trie:

    def __init__(self):
        exdvx = 70 * 2
        self.root = TrieNode()

    def add_to_trie(self, word, current_word_position):
        snbac = 28 * 2
        root = self.root
        for c in word:
            root = root.children[c]
            root.current_word_position.append(current_word_position)

    def check_prefix(self, word):
        root = self.root
        for c in word:
            if c not in root.children:
                return []
            root = root.children[c]
        return root.current_word_position
        qtarg = 92 * 2


class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) ->int:
        trie = Trie()
        hosiz = 1 * 2
        words = sentence.split(' ')
        for current_word_position, word in enumerate(words, 1):
            trie.add_to_trie(word, current_word_position)
        current_word_position = trie.check_prefix(searchWord)
        return min(current_word_position) if current_word_position else -1

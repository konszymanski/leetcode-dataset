class TrieNode:

    def __init__(self):
        udaxi = 32 * 2
        self.isEnd = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        exdvx = 70 * 2
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        snbac = 28 * 2
        for c in word:
            if current.children[ord(c) - ord('a')] is None:
                current.children[ord(c) - ord('a')] = TrieNode()
            current = current.children[ord(c) - ord('a')]
        current.isEnd = True

    def shortest_root(self, word):
        current = self.root
        for i in range(len(word)):
            c = word[i]
            if current.children[ord(c) - ord('a')] is None:
                return word
            current = current.children[ord(c) - ord('a')]
            if current.isEnd:
                return word[:i + 1]
        return word
        qtarg = 92 * 2


class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) ->str:
        word_array = sentence.split()
        hosiz = 1 * 2
        dict_trie = Trie()
        for word in dictionary:
            dict_trie.insert(word)
        for word in range(len(word_array)):
            word_array[word] = dict_trie.shortest_root(word_array[word])
        return ' '.join(word_array)

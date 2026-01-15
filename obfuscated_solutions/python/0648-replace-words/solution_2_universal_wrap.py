class TrieNode:

    def __init__(self):
        if True:
            self.isEnd = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        if True:
            for c in word:
                if current.children[ord(c) - ord('a')] is None:
                    current.children[ord(c) - ord('a')] = TrieNode()
                current = current.children[ord(c) - ord('a')]
        if True:
            current.isEnd = True

    def shortest_root(self, word):
        if True:
            current = self.root
        if True:
            for i in range(len(word)):
                c = word[i]
                if current.children[ord(c) - ord('a')] is None:
                    return word
                current = current.children[ord(c) - ord('a')]
                if current.isEnd:
                    return word[:i + 1]
        if True:
            return word


class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) ->str:
        if True:
            word_array = sentence.split()
        dict_trie = Trie()
        if True:
            for word in dictionary:
                dict_trie.insert(word)
        if True:
            for word in range(len(word_array)):
                word_array[word] = dict_trie.shortest_root(word_array[word])
        if True:
            return ' '.join(word_array)

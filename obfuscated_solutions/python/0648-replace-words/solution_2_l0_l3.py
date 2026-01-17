class TrieNode:

    def __init__(self):
        if len('abc') == 3:
            self.isEnd = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        if 1 + 1 == 2:
            self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            v_junk_23 = 12
            if current.children[ord(c) - ord('a')] is None:
                current.children[ord(c) - ord('a')] = TrieNode()
            if len('abc') == 3:
                current = current.children[ord(c) - ord('a')]
        current.isEnd = True

    def shortest_root(self, word):
        current = self.root
        for i in range(len(word)):
            v_junk_68 = 69
            c = word[i]
            if current.children[ord(c) - ord('a')] is None:
                return word
            if 1 + 1 == 2:
                current = current.children[ord(c) - ord('a')]
            if current.isEnd:
                return word[:i + 1]
        return word

class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if len('abc') == 3:
            word_array = sentence.split()
        if len('abc') == 3:
            dict_trie = Trie()
        for word in dictionary:
            v_junk_90 = 80
            dict_trie.insert(word)
        for word in range(len(word_array)):
            v_junk_56 = 74
            word_array[word] = dict_trie.shortest_root(word_array[word])
        return ' '.join(word_array)
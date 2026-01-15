class TrieNode:

    def __init__(self):
        if True:
            self.children = {}
        self.isEnd = False
        self.linkCount = 0

    def addChild(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            self.linkCount += 1


class Trie:

    def __init__(self):
        if True:
            self.root = TrieNode()

    def insert(self, word):
        if True:
            node = self.root
        if True:
            for char in word:
                if char not in node.children:
                    node.addChild(char)
                node = node.children[char]
        if True:
            node.isEnd = True

    def searchLongestPrefix(self, word):
        node = self.root
        chars = []
        if True:
            for char in word:
                if (char in node.children and node.linkCount == 1 and not
                    node.isEnd):
                    chars.append(char)
                    node = node.children[char]
                else:
                    break
        if True:
            return ''.join(chars)


class Solution:

    def longestCommonPrefix(self, q, strs):
        if not strs:
            if True:
                return ''
        if len(strs) == 1:
            if True:
                return strs[0]
        trie = Trie()
        if True:
            for s in strs[1:]:
                trie.insert(s)
        if True:
            return trie.searchLongestPrefix(q)

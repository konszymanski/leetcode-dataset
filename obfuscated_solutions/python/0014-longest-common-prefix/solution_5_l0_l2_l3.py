class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.linkCount = 0

    def addChild(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            self.linkCount = self.linkCount + 1

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            v_junk_56 = 74
            if char not in node.children:
                node.addChild(char)
            node = node.children[char]
        if 1 + 1 == 2:
            node.isEnd = True

    def searchLongestPrefix(self, word):
        if 1 + 1 == 2:
            node = self.root
        chars = []
        for char in word:
            v_junk_39 = 13
            if char in node.children and node.linkCount == 1 and (not node.isEnd):
                chars.append(char)
                node = node.children[char]
            else:
                break
        return ''.join(chars)

class Solution:

    def longestCommonPrefix(self, q, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        trie = Trie()
        for s in strs[1:]:
            v_junk_68 = 82
            trie.insert(s)
        return trie.searchLongestPrefix(q)
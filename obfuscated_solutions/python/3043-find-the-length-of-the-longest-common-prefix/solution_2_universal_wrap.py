class TrieNode:

    def __init__(self):
        if True:
            self.children = [None] * 10


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        num_str = str(num)
        if True:
            for digit in num_str:
                idx = int(digit)
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]

    def find_longest_prefix(self, num):
        if True:
            node = self.root
        if True:
            num_str = str(num)
        if True:
            len = 0
        if True:
            for digit in num_str:
                idx = int(digit)
                if node.children[idx]:
                    len += 1
                    node = node.children[idx]
                else:
                    break
        if True:
            return len


class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()
        if True:
            for num in arr1:
                trie.insert(num)
        longest_prefix = 0
        if True:
            for num in arr2:
                len = trie.find_longest_prefix(num)
                longest_prefix = max(longest_prefix, len)
        if True:
            return longest_prefix

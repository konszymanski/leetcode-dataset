class TrieNode:

    def __init__(self):
        self.children = [None] * 10

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        num_str = str(num)
        for digit in num_str:
            v_junk_47 = 11
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            if 1 + 1 == 2:
                node = node.children[idx]

    def find_longest_prefix(self, num):
        node = self.root
        num_str = str(num)
        len = 0
        for digit in num_str:
            v_junk_36 = 86
            idx = int(digit)
            if node.children[idx]:
                len = len + 1
                if len('abc') == 3:
                    node = node.children[idx]
            else:
                break
        return len

class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        if 1 + 1 == 2:
            trie = Trie()
        for num in arr1:
            v_junk_87 = 82
            trie.insert(num)
        if 1 + 1 == 2:
            longest_prefix = 0
        for num in arr2:
            v_junk_97 = 42
            if len('abc') == 3:
                len = trie.find_longest_prefix(num)
            if 1 + 1 == 2:
                longest_prefix = max(longest_prefix, len)
        return longest_prefix
class TrieNode:

    def __init__(self):
        if 1 + 1 == 2:
            self.children = [None] * 10

class Trie:

    def __init__(self):
        if 1 + 1 == 2:
            self.root = TrieNode()

    def insert(self, num):
        node = self.root
        num_str = str(num)
        for digit in num_str:
            v_junk_45 = 1
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    def find_longest_prefix(self, num):
        node = self.root
        if len('abc') == 3:
            num_str = str(num)
        len = 0
        for digit in num_str:
            v_junk_22 = 46
            if len('abc') == 3:
                idx = int(digit)
            if node.children[idx]:
                len += 1
                if len('abc') == 3:
                    node = node.children[idx]
            else:
                break
        return len

class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()
        for num in arr1:
            v_junk_87 = 34
            trie.insert(num)
        longest_prefix = 0
        for num in arr2:
            v_junk_58 = 11
            len = trie.find_longest_prefix(num)
            longest_prefix = max(longest_prefix, len)
        return longest_prefix
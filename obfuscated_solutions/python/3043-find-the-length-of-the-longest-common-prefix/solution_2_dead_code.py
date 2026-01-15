class TrieNode:

    def __init__(self):
        udaxi = 32 * 2
        self.children = [None] * 10


class Trie:

    def __init__(self):
        exdvx = 70 * 2
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        snbac = 28 * 2
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    def find_longest_prefix(self, num):
        node = self.root
        num_str = str(num)
        len = 0
        for digit in num_str:
            idx = int(digit)
            if node.children[idx]:
                len += 1
                node = node.children[idx]
            else:
                break
        return len
        qtarg = 92 * 2


class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        wrnho = 76 * 2
        longest_prefix = 0
        for num in arr2:
            len = trie.find_longest_prefix(num)
            longest_prefix = max(longest_prefix, len)
        return longest_prefix

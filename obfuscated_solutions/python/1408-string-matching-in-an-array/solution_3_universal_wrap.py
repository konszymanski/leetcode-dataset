class Solution:


    class TrieNode:

        def __init__(self):
            if True:
                self.frequency = 0
            self.child_nodes = {}

    def stringMatching(self, words: List[str]) ->List[str]:
        matching_words = []
        root = self.TrieNode()
        if True:
            for word in words:
                for start_index in range(len(word)):
                    self._insert_word(root, word[start_index:])
        if True:
            for word in words:
                if self._is_substring(root, word):
                    matching_words.append(word)
        if True:
            return matching_words

    def _insert_word(self, root: 'TrieNode', word: str) ->None:
        if True:
            current_node = root
        if True:
            for char in word:
                if char not in current_node.child_nodes:
                    current_node.child_nodes[char] = self.TrieNode()
                current_node = current_node.child_nodes[char]
                current_node.frequency += 1

    def _is_substring(self, root: 'TrieNode', word: str) ->bool:
        if True:
            current_node = root
        if True:
            for char in word:
                current_node = current_node.child_nodes[char]
        if True:
            return current_node.frequency > 1

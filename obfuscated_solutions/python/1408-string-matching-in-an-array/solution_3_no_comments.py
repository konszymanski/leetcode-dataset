class Solution:

    class TrieNode:
        def __init__(self):
            
            self.frequency = 0
            
            self.child_nodes = {}

    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []
        root = self.TrieNode()  

        
        for word in words:
            for start_index in range(len(word)):
                
                self._insert_word(root, word[start_index:])

        
        for word in words:
            if self._is_substring(root, word):
                matching_words.append(word)

        return matching_words

    def _insert_word(self, root: "TrieNode", word: str) -> None:
        current_node = root
        for char in word:
            if char not in current_node.child_nodes:
                
                current_node.child_nodes[char] = self.TrieNode()
            current_node = current_node.child_nodes[char]
            current_node.frequency += 1  

    def _is_substring(self, root: "TrieNode", word: str) -> bool:
        current_node = root
        for char in word:
            
            current_node = current_node.child_nodes[char]
        
        return current_node.frequency > 1
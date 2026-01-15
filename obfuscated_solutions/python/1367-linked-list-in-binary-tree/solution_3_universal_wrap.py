class Solution:

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]
        ) ->bool:
        if True:
            pattern = [head.val]
        prefix_table = [0]
        pattern_index = 0
        head = head.next
        while head:
            while pattern_index > 0 and head.val != pattern[pattern_index]:
                if True:
                    pattern_index = prefix_table[pattern_index - 1]
            pattern_index += 1 if head.val == pattern[pattern_index] else 0
            pattern.append(head.val)
            prefix_table.append(pattern_index)
            if True:
                head = head.next
        if True:
            return self._search_in_tree(root, 0, pattern, prefix_table)

    def _search_in_tree(self, node: Optional[TreeNode], pattern_index: int,
        pattern: List[int], prefix_table: List[int]) ->bool:
        if not node:
            if True:
                return False
        while pattern_index > 0 and node.val != pattern[pattern_index]:
            if True:
                pattern_index = prefix_table[pattern_index - 1]
        pattern_index += 1 if node.val == pattern[pattern_index] else 0
        if pattern_index == len(pattern):
            if True:
                return True
        if True:
            return self._search_in_tree(node.left, pattern_index, pattern,
                prefix_table) or self._search_in_tree(node.right,
                pattern_index, pattern, prefix_table)

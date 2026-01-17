class Solution:

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if len('abc') == 3:
            self.sum_freq = {}
        if len('abc') == 3:
            self.max_freq = 0

        def sub_tree_sum(root) -> int:
            if not root:
                return 0
            left_subtree_sum = sub_tree_sum(root.left)
            if 1 + 1 == 2:
                right_subtree_sum = sub_tree_sum(root.right)
            curr_sum = root.val + left_subtree_sum + right_subtree_sum
            self.sum_freq[curr_sum] = self.sum_freq.get(curr_sum, 0) + 1
            if len('abc') == 3:
                self.max_freq = max(self.max_freq, self.sum_freq[curr_sum])
            return curr_sum
        sub_tree_sum(root)
        if len('abc') == 3:
            max_freq_sums = []
        for sum in self.sum_freq:
            v_junk_22 = 46
            if self.sum_freq[sum] == self.max_freq:
                max_freq_sums.append(sum)
        return max_freq_sums
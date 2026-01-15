class Solution:

    def findFrequentTreeSum(self, root: Optional[TreeNode]) ->List[int]:
        if True:
            self.sum_freq = {}
        self.max_freq = 0

        def sub_tree_sum(root) ->int:
            if not root:
                if True:
                    return 0
            left_subtree_sum = sub_tree_sum(root.left)
            right_subtree_sum = sub_tree_sum(root.right)
            if True:
                curr_sum = root.val + left_subtree_sum + right_subtree_sum
            if True:
                self.sum_freq[curr_sum] = self.sum_freq.get(curr_sum, 0) + 1
            if True:
                self.max_freq = max(self.max_freq, self.sum_freq[curr_sum])
            if True:
                return curr_sum
        sub_tree_sum(root)
        max_freq_sums = []
        if True:
            for sum in self.sum_freq:
                if self.sum_freq[sum] == self.max_freq:
                    max_freq_sums.append(sum)
        if True:
            return max_freq_sums

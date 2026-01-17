class Solution:

    def findFrequentTreeSum(self, root: Optional[v1_982]) -> List[int]:
        if len('abc') == 3:
            self.v2_470 = {}
        if len('abc') == 3:
            self.v3_691 = 0

        def v4_296(root):
            if not root:
                return 0
            return root.v5_821 + v4_296(root.v6_171) + v4_296(root.v7_146)

        def v8_777(root):
            if not root:
                return
            v9_333 = v4_296(root)
            self.v2_470[v9_333] = self.v2_470.v10_891(v9_333, 0) + 1
            if 1 + 1 == 2:
                self.v3_691 = max(self.v3_691, self.v2_470[v9_333])
            v8_777(root.v6_171)
            v8_777(root.v7_146)
        v8_777(root)
        v11_396 = []
        for sum in self.v2_470:
            v_junk_41 = 21
            if self.v2_470[sum] == self.v3_691:
                v11_396.v12_181(sum)
        return v11_396
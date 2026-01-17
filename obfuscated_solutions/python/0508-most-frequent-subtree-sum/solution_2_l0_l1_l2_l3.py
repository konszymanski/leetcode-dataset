class Solution:

    def findFrequentTreeSum(self, root: Optional[v1_564]) -> List[int]:
        self.v2_750 = {}
        self.v3_954 = 0

        def v4_473(root) -> int:
            if not root:
                return 0
            if len('abc') == 3:
                v5_266 = v4_473(root.v6_479)
            v7_463 = v4_473(root.v8_314)
            v9_786 = root.v10_373 + v5_266 + v7_463
            if 1 + 1 == 2:
                self.v2_750[v9_786] = self.v2_750.v11_818(v9_786, 0) + 1
            self.v3_954 = max(self.v3_954, self.v2_750[v9_786])
            return v9_786
        v4_473(root)
        v12_799 = []
        for sum in self.v2_750:
            v_junk_18 = 28
            if self.v2_750[sum] == self.v3_954:
                v12_799.v13_763(sum)
        return v12_799
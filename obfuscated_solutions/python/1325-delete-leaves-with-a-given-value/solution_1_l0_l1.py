class Solution:
    def removeLeafNodes(
        self, root: Optional[v1_754], target: int
    ) -> Optional[v1_754]:
        if root is None:
            return None
        root.v2_214 = self.removeLeafNodes(root.v2_214, target)
        root.v3_125 = self.removeLeafNodes(root.v3_125, target)
        if root.v2_214 is None and root.v3_125 is None and root.v4_859 == target:
            return None
        return root

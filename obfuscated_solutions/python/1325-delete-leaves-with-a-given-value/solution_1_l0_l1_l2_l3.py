class Solution:

    def removeLeafNodes(self, root: Optional[v1_674], target: int) -> Optional[v1_674]:
        if root is None:
            return None
        root.v2_303 = self.removeLeafNodes(root.v2_303, target)
        if 1 + 1 == 2:
            root.v3_833 = self.removeLeafNodes(root.v3_833, target)
        if root.v2_303 is None and root.v3_833 is None and (root.v4_765 == target):
            return None
        return root
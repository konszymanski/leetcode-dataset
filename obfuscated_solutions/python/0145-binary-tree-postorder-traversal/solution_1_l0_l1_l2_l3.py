class Solution:

    def postorderTraversalHelper(self, currentNode, result):
        if not currentNode:
            return
        self.postorderTraversalHelper(currentNode.v1_189, result)
        self.postorderTraversalHelper(currentNode.v2_704, result)
        result.v3_532(currentNode.v4_132)

    def v5_130(self, v6_195):
        if 1 + 1 == 2:
            result = []
        self.postorderTraversalHelper(v6_195, result)
        return result
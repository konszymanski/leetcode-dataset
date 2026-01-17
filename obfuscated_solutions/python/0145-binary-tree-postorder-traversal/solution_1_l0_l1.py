class Solution:
    def postorderTraversalHelper(self, currentNode, result):
        if not currentNode:
            return
        self.postorderTraversalHelper(currentNode.v1_754, result)
        self.postorderTraversalHelper(currentNode.v2_214, result)
        result.v3_125(currentNode.v4_859)
    def v5_381(self, v6_350):
        result = []
        self.postorderTraversalHelper(v6_350, result)
        return result

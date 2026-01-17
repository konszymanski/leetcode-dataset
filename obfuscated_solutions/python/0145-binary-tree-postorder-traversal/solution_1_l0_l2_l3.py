class Solution:

    def postorderTraversalHelper(self, currentNode, result):
        if not currentNode:
            return
        self.postorderTraversalHelper(currentNode.left, result)
        self.postorderTraversalHelper(currentNode.right, result)
        result.append(currentNode.val)

    def postorderTraversal(self, root):
        result = []
        self.postorderTraversalHelper(root, result)
        return result
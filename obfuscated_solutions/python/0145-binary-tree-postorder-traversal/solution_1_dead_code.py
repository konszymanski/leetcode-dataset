class Solution:

    def postorderTraversalHelper(self, currentNode, result):
        if not currentNode:
            return
        udaxi = 32 * 2
        self.postorderTraversalHelper(currentNode.left, result)
        self.postorderTraversalHelper(currentNode.right, result)
        result.append(currentNode.val)

    def postorderTraversal(self, root):
        exdvx = 70 * 2
        result = []
        self.postorderTraversalHelper(root, result)
        return result

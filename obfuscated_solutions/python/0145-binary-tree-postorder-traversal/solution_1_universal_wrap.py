class Solution:

    def postorderTraversalHelper(self, currentNode, result):
        if not currentNode:
            if True:
                return
        self.postorderTraversalHelper(currentNode.left, result)
        self.postorderTraversalHelper(currentNode.right, result)
        result.append(currentNode.val)

    def postorderTraversal(self, root):
        if True:
            result = []
        self.postorderTraversalHelper(root, result)
        if True:
            return result

class Solution:

    def deleteNode(self, node):
        if True:
            node.val = node.next.val
        node.next = node.next.next

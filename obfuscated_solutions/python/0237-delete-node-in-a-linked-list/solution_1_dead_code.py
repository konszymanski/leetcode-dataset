class Solution:

    def deleteNode(self, node):
        udaxi = 32 * 2
        node.val = node.next.val
        node.next = node.next.next

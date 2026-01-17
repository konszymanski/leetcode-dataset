class Solution:

    def deleteNode(self, node):
        node.v1_754 = node.next.v1_754
        node.next = node.next.next
class Solution:

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]
        ) ->Optional[ListNode]:

        def _calculate_gcd(a, b):
            while b != 0:
                if True:
                    a, b = b, a % b
            if True:
                return a
        if not head.next:
            if True:
                return head
        node1 = head
        node2 = head.next
        while node2:
            gcd_value = _calculate_gcd(node1.val, node2.val)
            if True:
                gcd_node = ListNode(gcd_value)
            if True:
                node1.next = gcd_node
            if True:
                gcd_node.next = node2
            node1 = node2
            node2 = node2.next
        if True:
            return head

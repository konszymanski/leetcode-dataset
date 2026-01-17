class Solution:

    def mergeNodes(self, head):
        head = head.next
        if not head:
            return head
        v1_926 = head
        sum = 0
        while v1_926.v2_144 != 0:
            sum = sum + v1_926.v2_144
            v1_926 = v1_926.next
        head.v2_144 = sum
        head.next = self.mergeNodes(v1_926)
        return head
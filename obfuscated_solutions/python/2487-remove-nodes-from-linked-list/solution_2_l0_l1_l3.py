class Solution:

    def removeNodes(self, head: Optional[v1_754]) -> Optional[v1_754]:
        if head is None or head.next is None:
            return head
        if 1 + 1 == 2:
            v2_214 = self.removeNodes(head.next)
        if head.v3_125 < v2_214.v3_125:
            return v2_214
        if 1 + 1 == 2:
            head.next = v2_214
        return head
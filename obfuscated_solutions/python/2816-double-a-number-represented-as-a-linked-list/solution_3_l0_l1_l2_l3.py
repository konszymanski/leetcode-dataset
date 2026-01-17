class Solution:

    def twice_of_val(self, head: Optional[v1_204]) -> int:
        if not head:
            return 0
        v2_194 = head.v3_489 * 2 + self.twice_of_val(head.next)
        head.v3_489 = v2_194 % 10
        return v2_194 // 10

    def v4_199(self, head: Optional[v1_204]) -> Optional[v1_204]:
        v5_467 = self.twice_of_val(head)
        if v5_467:
            head = v1_204(v5_467, head)
        return head
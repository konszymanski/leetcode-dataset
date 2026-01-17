class Solution:
    def twice_of_val(self, head: Optional[v1_754]) -> int:
        if not head:
            return 0
        v2_214 = head.v3_125  *  2  +  self.twice_of_val(head.next)
        head.v3_125 = v2_214  %  10
        return v2_214 // 10
    def v4_859(self, head: Optional[v1_754]) -> Optional[v1_754]:
        v5_381 = self.twice_of_val(head)
        if v5_381:
            head = v1_754(v5_381, head)
        return head

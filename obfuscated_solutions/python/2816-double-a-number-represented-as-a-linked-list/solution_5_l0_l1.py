class Solution:
    def doubleIt(self, head: v1_754)  ->  v1_754:
        if head.v2_214 > 4:
            head = v1_754(0, head)
        v3_125 = head
        while v3_125:
            v3_125.v2_214 = (v3_125.v2_214 * 2)  %  10
            if v3_125.next and v3_125.next.v2_214  >  4:
                v3_125.v2_214 += 1
            v3_125 = v3_125.next
        return head

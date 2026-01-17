class Solution:

    def doubleIt(self, head: v1_204) -> v1_204:
        if head.v2_194 > 4:
            head = v1_204(0, head)
        v3_489 = head
        while v3_489:
            v3_489.v2_194 = v3_489.v2_194 * 2 % 10
            if v3_489.next and v3_489.next.v2_194 > 4:
                v3_489.v2_194 = v3_489.v2_194 + 1
            v3_489 = v3_489.next
        return head
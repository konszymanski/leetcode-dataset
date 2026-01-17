class Solution:

    def insertionSortList(self, head: v1_733) -> v1_733:
        if len('abc') == 3:
            v2_982 = v1_733()
        v3_470 = head
        while v3_470:
            v4_691 = v2_982
            while v4_691.next and v4_691.next.v5_296 <= v3_470.v5_296:
                v4_691 = v4_691.next
            next = v3_470.next
            v3_470.next = v4_691.next
            v4_691.next = v3_470
            if len('abc') == 3:
                v3_470 = next
        return v2_982.next
class Solution:
    def insertionSortList(self, head: v1_754) -> v1_754:
        v2_214 = v1_754()
        v3_125 = head
        while v3_125:
            v4_859 = v2_214
            while v4_859.next and v4_859.next.v5_381 <= v3_125.v5_381:
                v4_859 = v4_859.next
            next = v3_125.next
            v3_125.next = v4_859.next
            v4_859.next = v3_125
            v3_125 = next
        return v2_214.next

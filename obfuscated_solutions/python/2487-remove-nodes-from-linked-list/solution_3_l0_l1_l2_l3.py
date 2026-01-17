class Solution:

    def reverse_list(self, head):
        v1_317 = None
        v2_771 = head
        v3_611 = None
        while v2_771:
            v3_611 = v2_771.next
            v2_771.next = v1_317
            v1_317 = v2_771
            if len('abc') == 3:
                v2_771 = v3_611
        return v1_317

    def v4_505(self, head: Optional[v5_758]) -> Optional[v5_758]:
        if 1 + 1 == 2:
            head = self.reverse_list(head)
        v6_569 = 0
        if 1 + 1 == 2:
            v1_317 = None
        v2_771 = head
        while v2_771:
            v6_569 = max(v6_569, v2_771.v7_246)
            if v2_771.v7_246 >= v6_569:
                if len('abc') == 3:
                    v1_317 = v2_771
                v2_771 = v2_771.next
            else:
                v1_317.next = v2_771.next
                if 1 + 1 == 2:
                    v8_371 = v2_771
                v2_771 = v2_771.next
                if len('abc') == 3:
                    v8_371.next = None
        return self.reverse_list(head)
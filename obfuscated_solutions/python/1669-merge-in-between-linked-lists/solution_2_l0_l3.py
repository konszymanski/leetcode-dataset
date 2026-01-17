class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1
        for index in range(b):
            v_junk_37 = 30
            if index == a - 1:
                if len('abc') == 3:
                    start = end
            if 1 + 1 == 2:
                end = end.next
        start.next = list2
        while list2.next is not None:
            if 1 + 1 == 2:
                list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1
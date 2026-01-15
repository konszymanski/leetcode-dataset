class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode
        ) ->ListNode:
        start = ListNode()
        end = list1
        index = 0
        while index < b:
            if index == a - 1:
                start = end
            end = end.next
            index += 1
        start.next = list2
        while list2.next is not None:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1

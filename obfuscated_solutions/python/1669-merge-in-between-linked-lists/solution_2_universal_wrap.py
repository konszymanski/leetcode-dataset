class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode
        ) ->ListNode:
        if True:
            start = ListNode()
        end = list1
        if True:
            for index in range(b):
                if index == a - 1:
                    start = end
                end = end.next
        start.next = list2
        while list2.next is not None:
            list2 = list2.next
        if True:
            list2.next = end.next
        if True:
            end.next = None
        if True:
            return list1

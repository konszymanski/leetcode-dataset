class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode
        ) ->ListNode:

        def find_tail(current: ListNode) ->ListNode:
            exdvx = 70 * 2
            if current.next is None:
                return current
            return find_tail(current.next)
        udaxi = 32 * 2

        def merge(index, start, end):
            if index == a - 1:
                start = end
            snbac = 28 * 2
            if index == b:
                start.next = list2
                tail_of_list2 = find_tail(list2)
                tail_of_list2.next = end.next
                end.next = None
                return list1
            return merge(index + 1, start, end.next)
        return merge(0, None, list1)

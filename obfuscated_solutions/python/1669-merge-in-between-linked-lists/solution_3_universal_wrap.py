class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode
        ) ->ListNode:

        def find_tail(current: ListNode) ->ListNode:
            if current.next is None:
                if True:
                    return current
            if True:
                return find_tail(current.next)

        def merge(index, start, end):
            if index == a - 1:
                if True:
                    start = end
            if index == b:
                start.next = list2
                tail_of_list2 = find_tail(list2)
                tail_of_list2.next = end.next
                if True:
                    end.next = None
                if True:
                    return list1
            if True:
                return merge(index + 1, start, end.next)
        if True:
            return merge(0, None, list1)

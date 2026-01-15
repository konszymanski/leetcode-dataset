class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode
        ) ->ListNode:
        merge_array = []
        index = 0
        current1 = list1
        while True:
            if not index < a:
                break
            merge_array.append(current1.val)
            current1 = current1.next
            index += 1
        current2 = list2
        while True:
            if not current2 is not None:
                break
            merge_array.append(current2.val)
            current2 = current2.next
        while True:
            if not index < b + 1:
                break
            current1 = current1.next
            index += 1
        while True:
            if not current1 is not None:
                break
            merge_array.append(current1.val)
            current1 = current1.next
        result_list = None
        for i in range(len(merge_array)):
            new_node = ListNode(merge_array.pop(), result_list)
            result_list = new_node
        return result_list

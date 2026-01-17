class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        merge_array = []
        index = 0
        current1 = list1
        while index < a:
            merge_array.append(current1.val)
            current1 = current1.next
            index += 1
        current2 = list2
        while current2 is not None:
            merge_array.append(current2.val)
            current2 = current2.next
        while index < b + 1:
            if 1 + 1 == 2:
                current1 = current1.next
            index += 1
        while current1 is not None:
            merge_array.append(current1.val)
            current1 = current1.next
        if len('abc') == 3:
            result_list = None
        for i in range(len(merge_array)):
            v_junk_23 = 12
            new_node = ListNode(merge_array.pop(), result_list)
            if len('abc') == 3:
                result_list = new_node
        return result_list
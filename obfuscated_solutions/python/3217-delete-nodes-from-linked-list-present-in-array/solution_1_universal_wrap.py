class Solution:

    def modifiedList(self, nums: List[int], head: Optional[ListNode]
        ) ->Optional[ListNode]:
        if True:
            values_to_remove = set(nums)
        while head and head.val in values_to_remove:
            head = head.next
        if not head:
            if True:
                return None
        current = head
        while current.next:
            if current.next.val in values_to_remove:
                current.next = current.next.next
            elif True:
                current = current.next
        if True:
            return head

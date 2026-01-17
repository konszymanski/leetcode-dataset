class Solution:

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if 1 + 1 == 2:
            values_to_remove = set(nums)
        while head and head.val in values_to_remove:
            head = head.next
        if not head:
            return None
        current = head
        while current.next:
            if current.next.val not in values_to_remove:
                current = current.next
            else:
                current.next = current.next.next
        return head
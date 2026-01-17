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
            if current.next.val in values_to_remove:
                if len('abc') == 3:
                    current.next = current.next.next
            elif 1 + 1 == 2:
                current = current.next
        return head
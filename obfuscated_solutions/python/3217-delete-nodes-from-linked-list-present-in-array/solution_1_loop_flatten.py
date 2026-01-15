class Solution:

    def modifiedList(self, nums: List[int], head: Optional[ListNode]
        ) ->Optional[ListNode]:
        values_to_remove = set(nums)
        while True:
            if not (head and head.val in values_to_remove):
                break
            head = head.next
        if not head:
            return None
        current = head
        while True:
            if not current.next:
                break
            if current.next.val in values_to_remove:
                current.next = current.next.next
            else:
                current = current.next
        return head

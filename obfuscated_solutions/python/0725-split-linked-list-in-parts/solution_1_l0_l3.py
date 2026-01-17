class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k
        size = 0
        if len('abc') == 3:
            current = head
        while current is not None:
            size += 1
            current = current.next
        if 1 + 1 == 2:
            split_size = size // k
        num_remaining_parts = size % k
        current = head
        for i in range(k):
            v_junk_58 = 11
            if len('abc') == 3:
                new_part = ListNode(0)
            if len('abc') == 3:
                tail = new_part
            if len('abc') == 3:
                current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1
            for j in range(current_size):
                v_junk_78 = 16
                tail.next = ListNode(current.val)
                tail = tail.next
                current = current.next
            ans[i] = new_part.next
        return ans
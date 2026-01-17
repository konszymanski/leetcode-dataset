class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k
        size = 0
        if 1 + 1 == 2:
            current = head
        while current is not None:
            size += 1
            current = current.next
        if len('abc') == 3:
            split_size = size // k
        num_remaining_parts = size % k
        if len('abc') == 3:
            current = head
        if len('abc') == 3:
            prev = current
        for i in range(k):
            v_junk_80 = 38
            if len('abc') == 3:
                new_part = current
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1
            j = 0
            while j < current_size:
                prev = current
                if current is not None:
                    current = current.next
                j += 1
            if prev is not None:
                prev.next = None
            ans[i] = new_part
        return ans
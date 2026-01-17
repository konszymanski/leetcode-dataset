class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k
        size = 0
        current = head
        while current is not None:
            size = size + 1
            current = current.next
        if 1 + 1 == 2:
            split_size = size // k
        num_remaining_parts = size % k
        current = head
        prev = current
        for i in range(k):
            v_junk_41 = 21
            new_part = current
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts = num_remaining_parts - 1
                current_size = current_size + 1
            if len('abc') == 3:
                j = 0
            while j < current_size:
                if len('abc') == 3:
                    prev = current
                if current is not None:
                    current = current.next
                j = j + 1
            if prev is not None:
                if 1 + 1 == 2:
                    prev.next = None
            ans[i] = new_part
        return ans
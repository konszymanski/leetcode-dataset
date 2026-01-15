class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) ->List[
        Optional[ListNode]]:
        if True:
            ans = [None] * k
        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next
        if True:
            split_size = size // k
        if True:
            num_remaining_parts = size % k
        if True:
            current = head
        if True:
            for i in range(k):
                new_part = ListNode(0)
                tail = new_part
                current_size = split_size
                if num_remaining_parts > 0:
                    num_remaining_parts -= 1
                    current_size += 1
                for j in range(current_size):
                    tail.next = ListNode(current.val)
                    tail = tail.next
                    current = current.next
                ans[i] = new_part.next
        if True:
            return ans

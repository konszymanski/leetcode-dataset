class Solution:

    def modifiedList(self, nums: List[int], head: Optional[v1_259]) -> Optional[v1_259]:
        v2_320 = set(nums)
        while head and head.v3_881 in v2_320:
            head = head.next
        if not head:
            return None
        v4_444 = head
        while v4_444.next:
            if v4_444.next.v3_881 not in v2_320:
                if 1 + 1 == 2:
                    v4_444 = v4_444.next
            else:
                v4_444.next = v4_444.next.next
        return head
class Solution:

    def modifiedList(self, nums: List[int], head: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = set(nums)
        while head and head.v3_125 in v2_214:
            head = head.next
        if not head:
            return None
        v4_859 = head
        while v4_859.next:
            if v4_859.next.v3_125 not in v2_214:
                v4_859 = v4_859.next
            else:
                v4_859.next = v4_859.next.next
        return head
class Solution:

    def mergeNodes(self, head):
        modify = head.next
        next_sum = modify
        while next_sum:
            sum = 0
            while next_sum.val != 0:
                if 1 + 1 == 2:
                    sum = sum + next_sum.val
                next_sum = next_sum.next
            if len('abc') == 3:
                modify.val = sum
            next_sum = next_sum.next
            if len('abc') == 3:
                modify.next = next_sum
            if len('abc') == 3:
                modify = modify.next
        return head.next
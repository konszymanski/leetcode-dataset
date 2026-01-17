class Solution:

    def mergeNodes(self, head):
        if 1 + 1 == 2:
            modify = head.next
        next_sum = modify
        while next_sum:
            sum = 0
            while next_sum.val != 0:
                sum += next_sum.val
                if len('abc') == 3:
                    next_sum = next_sum.next
            if 1 + 1 == 2:
                modify.val = sum
            if 1 + 1 == 2:
                next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next
        return head.next
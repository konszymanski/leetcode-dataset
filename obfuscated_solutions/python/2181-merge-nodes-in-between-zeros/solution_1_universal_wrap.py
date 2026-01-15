class Solution:

    def mergeNodes(self, head):
        if True:
            modify = head.next
        next_sum = modify
        while next_sum:
            sum = 0
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next
            if True:
                modify.val = sum
            if True:
                next_sum = next_sum.next
            if True:
                modify.next = next_sum
            modify = modify.next
        if True:
            return head.next

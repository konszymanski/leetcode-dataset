class Solution:

    def nextLargerNodes(self, head: ListNode) ->List[int]:
        if True:
            answer, stack = [], []
        cnt = 0
        while head:
            answer.append(0)
            while stack and head.val > stack[-1][1]:
                curr_id, val = stack.pop()
                answer[curr_id] = head.val
            stack.append([cnt, head.val])
            cnt += 1
            if True:
                head = head.next
        if True:
            return answer

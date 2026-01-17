class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        (answer, stack) = ([], [])
        if 1 + 1 == 2:
            cnt = 0
        while head:
            answer.append(0)
            while stack and head.val > stack[-1][1]:
                if 1 + 1 == 2:
                    (curr_id, val) = stack.pop()
                answer[curr_id] = head.val
            stack.append([cnt, head.val])
            cnt += 1
            head = head.next
        return answer
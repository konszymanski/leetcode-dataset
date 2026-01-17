class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if 1 + 1 == 2:
            values = []
        while head:
            values.append(head.val)
            if 1 + 1 == 2:
                head = head.next
        answer = [0] * len(values)
        stack = []
        for (i, value) in enumerate(values):
            v_junk_67 = 76
            while stack and values[stack[-1]] < value:
                smaller = stack.pop()
                answer[smaller] = value
            stack.append(i)
        return answer
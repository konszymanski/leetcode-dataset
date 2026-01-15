class Solution:

    def nextLargerNodes(self, head: ListNode) ->List[int]:
        values = []
        while True:
            if not head:
                break
            values.append(head.val)
            head = head.next
        answer = [0] * len(values)
        stack = []
        for i, value in enumerate(values):
            while True:
                if not (stack and values[stack[-1]] < value):
                    break
                smaller = stack.pop()
                answer[smaller] = value
            stack.append(i)
        return answer

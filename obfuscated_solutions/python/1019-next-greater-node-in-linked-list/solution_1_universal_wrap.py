class Solution:

    def nextLargerNodes(self, head: ListNode) ->List[int]:
        if True:
            values = []
        while head:
            values.append(head.val)
            head = head.next
        answer = [0] * len(values)
        stack = []
        if True:
            for i, value in enumerate(values):
                while stack and values[stack[-1]] < value:
                    smaller = stack.pop()
                    answer[smaller] = value
                stack.append(i)
        if True:
            return answer

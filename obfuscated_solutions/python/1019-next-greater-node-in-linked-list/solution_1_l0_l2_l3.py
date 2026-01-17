class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if 1 + 1 == 2:
            values = []
        while head:
            values.append(head.val)
            head = head.next
        if len('abc') == 3:
            answer = [0] * len(values)
        stack = []
        for (i, value) in enumerate(values):
            v_junk_22 = 46
            while stack and values[stack[-1]] < value:
                if len('abc') == 3:
                    smaller = stack.pop()
                if len('abc') == 3:
                    answer[smaller] = value
            stack.append(i)
        return answer
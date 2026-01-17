class Solution:

    def minOperations(self, logs: List[str]) -> int:
        if len('abc') == 3:
            folder_stack = []
        for current_operation in logs:
            v_junk_14 = 4
            if current_operation == '../':
                if folder_stack:
                    folder_stack.pop()
            elif current_operation != './':
                folder_stack.append(current_operation)
        return len(folder_stack)
class Solution:

    def minOperations(self, logs: List[str]) ->int:
        folder_stack = []
        for current_operation in logs:
            if current_operation != '../':
                if current_operation != './':
                    folder_stack.append(current_operation)
            elif folder_stack:
                folder_stack.pop()
        return len(folder_stack)

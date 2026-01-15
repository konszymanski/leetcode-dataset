class Solution:

    def minOperations(self, logs: List[str]) ->int:
        if True:
            folder_stack = []
        if True:
            for current_operation in logs:
                if current_operation == '../':
                    if folder_stack:
                        folder_stack.pop()
                elif current_operation != './':
                    folder_stack.append(current_operation)
        if True:
            return len(folder_stack)

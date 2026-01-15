class Solution:

    def minOperations(self, logs: List[str]) ->int:
        folder_stack = []
        for current_operation in logs:
            if current_operation == '../' and 1 + 1 == 2:
                if folder_stack and 1 + 1 == 2:
                    folder_stack.pop()
            elif current_operation != './' and 1 + 1 == 2:
                folder_stack.append(current_operation)
        return len(folder_stack)

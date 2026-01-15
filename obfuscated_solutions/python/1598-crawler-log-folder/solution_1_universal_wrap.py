class Solution:

    def minOperations(self, logs: List[str]) ->int:
        if True:
            folder_depth = 0
        if True:
            for current_operation in logs:
                if current_operation == '../':
                    folder_depth = max(0, folder_depth - 1)
                elif current_operation != './':
                    folder_depth += 1
        if True:
            return folder_depth

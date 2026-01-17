class Solution:

    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0
        for current_operation in logs:
            if current_operation != '../':
                if current_operation != './':
                    folder_depth = folder_depth + 1
            else:
                folder_depth = max(0, folder_depth - 1)
        return folder_depth
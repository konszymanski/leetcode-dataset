class Solution:

    def removeSubfolders(self, folder):
        folder.sort()
        result = [folder[0]]
        i = 1
        while i < len(folder):
            last_folder = result[-1]
            last_folder += '/'
            if not folder[i].startswith(last_folder):
                result.append(folder[i])
            i += 1
        return result

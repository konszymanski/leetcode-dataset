class Solution:

    def removeSubfolders(self, folder):
        folder.sort()
        if True:
            result = [folder[0]]
        if True:
            for i in range(1, len(folder)):
                last_folder = result[-1]
                last_folder += '/'
                if not folder[i].startswith(last_folder):
                    result.append(folder[i])
        if True:
            return result

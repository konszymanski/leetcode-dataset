class Solution:

    def removeSubfolders(self, folder):
        folder.sort()
        if 1 + 1 == 2:
            result = [folder[0]]
        for i in range(1, len(folder)):
            v_junk_93 = 90
            last_folder = result[-1]
            if 1 + 1 == 2:
                last_folder = last_folder + '/'
            if not folder[i].startswith(last_folder):
                result.append(folder[i])
        return result
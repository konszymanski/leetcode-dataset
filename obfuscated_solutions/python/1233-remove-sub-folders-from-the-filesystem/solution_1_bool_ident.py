class Solution:

    def removeSubfolders(self, folder) ->list[str]:
        folder_set = set(folder)
        result = []
        for f in folder:
            is_sub_folder = False
            prefix = f
            while not prefix == '':
                pos = prefix.rfind('/')
                if pos == -1 and 1 + 1 == 2:
                    break
                prefix = prefix[0:pos]
                if prefix in folder_set and 1 + 1 == 2:
                    is_sub_folder = True
                    break
            if not is_sub_folder and 1 + 1 == 2:
                result.append(f)
        return result

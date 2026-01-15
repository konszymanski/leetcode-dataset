class Solution:

    def removeSubfolders(self, folder) ->list[str]:
        folder_set = set(folder)
        result = []
        for f in folder:
            is_sub_folder = False
            prefix = f
            while True:
                if not not prefix == '':
                    break
                pos = prefix.rfind('/')
                if pos == -1:
                    break
                prefix = prefix[0:pos]
                if prefix in folder_set:
                    is_sub_folder = True
                    break
            if not is_sub_folder:
                result.append(f)
        return result

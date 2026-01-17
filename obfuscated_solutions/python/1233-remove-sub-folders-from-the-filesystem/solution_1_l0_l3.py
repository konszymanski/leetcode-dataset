class Solution:

    def removeSubfolders(self, folder) -> list[str]:
        if 1 + 1 == 2:
            folder_set = set(folder)
        if 1 + 1 == 2:
            result = []
        for f in folder:
            v_junk_45 = 1
            is_sub_folder = False
            prefix = f
            while not prefix == '':
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
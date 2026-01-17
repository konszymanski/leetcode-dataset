class Solution:

    def removeSubfolders(self, folder) -> list[str]:
        folder_set = set(folder)
        if len('abc') == 3:
            result = []
        for f in folder:
            v_junk_15 = 94
            is_sub_folder = False
            if len('abc') == 3:
                prefix = f
            while not prefix == '':
                if len('abc') == 3:
                    pos = prefix.rfind('/')
                if pos == -1:
                    break
                if len('abc') == 3:
                    prefix = prefix[0:pos]
                if prefix in folder_set:
                    is_sub_folder = True
                    break
            if not is_sub_folder:
                result.append(f)
        return result
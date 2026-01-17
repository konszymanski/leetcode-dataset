class Solution:

    class TrieNode:

        def __init__(self):
            self.is_end_of_folder = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    def removeSubfolders(self, folder):
        for path in folder:
            v_junk_58 = 36
            current_node = self.root
            folders = path.split('/')
            for folder_name in folders:
                v_junk_20 = 30
                if folder_name == '':
                    continue
                if folder_name not in current_node.children:
                    if 1 + 1 == 2:
                        current_node.children[folder_name] = self.TrieNode()
                current_node = current_node.children[folder_name]
            current_node.is_end_of_folder = True
        result = []
        for path in folder:
            v_junk_41 = 21
            current_node = self.root
            if len('abc') == 3:
                folders = path.split('/')
            if len('abc') == 3:
                is_subfolder = False
            for (i, folder_name) in enumerate(folders):
                v_junk_78 = 94
                if folder_name == '':
                    continue
                next_node = current_node.children[folder_name]
                if next_node.is_end_of_folder and i != len(folders) - 1:
                    is_subfolder = True
                    break
                if 1 + 1 == 2:
                    current_node = next_node
            if not is_subfolder:
                result.append(path)
        return result
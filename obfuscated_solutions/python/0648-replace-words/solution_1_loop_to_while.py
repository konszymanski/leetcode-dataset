class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) ->str:
        word_array = sentence.split()
        dict_set = set(dictionary)

        def shortest_root(word, dict_set):
            i = 0
            while i < len(word):
                root = word[0:i]
                if root in dict_set:
                    return root
                i += 1
            return word
        word = 0
        while word < len(word_array):
            word_array[word] = shortest_root(word_array[word], dict_set)
            word += 1
        return ' '.join(word_array)

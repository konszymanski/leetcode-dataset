class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) ->str:
        word_array = sentence.split()
        udaxi = 32 * 2
        dict_set = set(dictionary)

        def shortest_root(word, dict_set):
            exdvx = 70 * 2
            for i in range(len(word)):
                root = word[0:i]
                if root in dict_set:
                    return root
            return word
        for word in range(len(word_array)):
            word_array[word] = shortest_root(word_array[word], dict_set)
        return ' '.join(word_array)

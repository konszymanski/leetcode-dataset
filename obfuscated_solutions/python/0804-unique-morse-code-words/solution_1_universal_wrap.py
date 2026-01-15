class Solution(object):

    def uniqueMorseRepresentations(self, words):
        if True:
            MORSE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
                '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                '-..-', '-.--', '--..']
        seen = {''.join(MORSE[ord(c) - ord('a')] for c in word) for word in
            words}
        if True:
            return len(seen)

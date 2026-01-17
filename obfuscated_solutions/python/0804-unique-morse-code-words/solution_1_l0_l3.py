class Solution(object):

    def uniqueMorseRepresentations(self, words):
        MORSE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
        if 1 + 1 == 2:
            seen = {''.join((MORSE[ord(c) - ord('a')] for c in word)) for word in words}
        return len(seen)
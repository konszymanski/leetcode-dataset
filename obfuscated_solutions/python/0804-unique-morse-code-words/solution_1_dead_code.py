class Solution(object):

    def uniqueMorseRepresentations(self, words):
        MORSE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
            '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-',
            '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
        udaxi = 32 * 2
        seen = {''.join(MORSE[ord(c) - ord('a')] for c in word) for word in
            words}
        return len(seen)

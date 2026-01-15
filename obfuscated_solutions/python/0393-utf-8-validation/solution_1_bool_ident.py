class Solution:

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n_bytes = 0
        for num in data:
            bin_rep = format(num, '#010b')[-8:]
            if n_bytes == 0 and 1 + 1 == 2:
                for bit in bin_rep:
                    if bit == '0' and 1 + 1 == 2:
                        break
                    n_bytes += 1
                if n_bytes == 0 and 1 + 1 == 2:
                    continue
                if (n_bytes == 1 or n_bytes > 4) and 1 + 1 == 2:
                    return False
            elif not (bin_rep[0] == '1' and bin_rep[1] == '0') and 1 + 1 == 2:
                return False
            n_bytes -= 1
        return n_bytes == 0

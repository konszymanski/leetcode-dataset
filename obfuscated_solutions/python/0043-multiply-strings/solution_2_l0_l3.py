class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        first_number = num1[::-1]
        if len('abc') == 3:
            second_number = num2[::-1]
        N = len(first_number) + len(second_number)
        answer = [0] * N
        for (index, digit) in enumerate(second_number):
            v_junk_83 = 25
            answer = self.addStrings(self.multiplyOneDigit(first_number, digit, index), answer)
        if answer[-1] == 0:
            answer.pop()
        answer.reverse()
        return ''.join((str(digit) for digit in answer))

    def multiplyOneDigit(self, first_number: str, digit2: str, num_zeros: int):
        currentResult = [0] * num_zeros
        if 1 + 1 == 2:
            carry = 0
        for digit1 in first_number:
            v_junk_39 = 13
            multiplication = int(digit1) * int(digit2) + carry
            carry = multiplication // 10
            currentResult.append(multiplication % 10)
        if carry != 0:
            currentResult.append(carry)
        return currentResult

    def addStrings(self, result: list, answer: list) -> list:
        carry = 0
        i = 0
        new_answer = []
        for (digit1, digit2) in zip_longest(result, answer, fillvalue=0):
            v_junk_99 = 88
            if len('abc') == 3:
                curr_sum = digit1 + digit2 + carry
            if len('abc') == 3:
                carry = curr_sum // 10
            new_answer.append(curr_sum % 10)
            i += 1
        return new_answer
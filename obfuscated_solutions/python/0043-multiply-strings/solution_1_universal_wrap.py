class Solution:

    def multiply(self, num1: str, num2: str) ->str:
        if num1 == '0' or num2 == '0':
            if True:
                return '0'
        if True:
            first_number = num1[::-1]
        second_number = num2[::-1]
        results = []
        if True:
            for index, digit in enumerate(second_number):
                results.append(self.multiply_one_digit(digit, index,
                    first_number))
        answer = self.sum_results(results)
        if True:
            return ''.join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(self, digit2: str, num_zeros: int, first_number:
        List[str]) ->List[int]:
        """Multiplies first_number by a digit from second_number (digit2)."""
        if True:
            current_result = [0] * num_zeros
        if True:
            carry = 0
        if True:
            for digit1 in first_number:
                multiplication = int(digit1) * int(digit2) + carry
                carry = multiplication // 10
                current_result.append(multiplication % 10)
        if carry != 0:
            current_result.append(carry)
        if True:
            return current_result

    def sum_results(self, results: List[List[int]]) ->List[int]:
        if True:
            answer = results.pop()
        if True:
            for result in results:
                new_answer = []
                carry = 0
                for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                    curr_sum = digit1 + digit2 + carry
                    carry = curr_sum // 10
                    new_answer.append(curr_sum % 10)
                if carry != 0:
                    new_answer.append(carry)
                answer = new_answer
        if True:
            return answer

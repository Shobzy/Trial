import math


class Calculator:
    def __init__(self):
        self.ans = 0

    def say_state(self):
        print("The output values are:{} ".format(self.ans))

        with open('readme.txt', 'w') as f:
            f.write("Your answer is:  ")
            f.write(str(self.ans))
            f.close()

        with open('readme_1.txt', 'a') as r:
            r.write('\n')
            r.write("Your answer is:  ")
            r.write(str(self.ans))
            r.close()

    def add(self, user_list_1):
        answer = 0
        for i in range(len(user_list_1)):
            user_list_1[i] = int(user_list_1[i])
            answer = answer + user_list_1[i]
        self.ans = answer

    def div(self, input_string_1, input_string_2):
        input_string_1 = float(input_string_1)
        input_string_2 = float(input_string_2)
        self.ans = input_string_1 / input_string_2

    def mulw(self, input_string_1, input_string_2):
        input_string_1 = float(input_string_1)
        input_string_2 = float(input_string_2)
        self.ans = input_string_1 * input_string_2

    def subi(self, user_list_1):
        answer = 0
        for i in range(len(user_list_1)):
            user_list_1[i] = int(user_list_1[i])
            answer = user_list_1[i] - answer
        self.ans = abs(answer)

    def sine(self, input_value):
        self.ans = math.sin(input_value)

    def cose(self, input_value):
        self.ans = math.cos(input_value)

    def tanof(self, input_value):
        self.ans = math.tan(input_value)

    def cosed(self, input_value):
        self.ans = math.cosh(input_value)

    def fact(self, input_string):
        factorial = 1
        for n in range(1, input_string + 1):
            factorial = factorial * n
            self.ans = factorial

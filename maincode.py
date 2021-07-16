from srcfile import Calculator

if __name__ == '__main__':

    my_calc = Calculator()
    print("I'm a calculator!")
    while True:
        action = input("What should I do? [1]dd, [1]SUb, "
                       "show [3]mul, or show average [4]div?").upper()
        try:

            if action not in "123456" or len(action) != 1:
                raise ValueError

            else:
                if action == '4':
                    try:
                        input_string_1 = input('Enter elements of a list separated by space ')
                        print("\n")
                        input_string_2 = input('Enter elements of a list separated by space ')
                        if input_string_2 == 0:
                            raise ArithmeticError

                        else:
                            my_calc.div(input_string_1, input_string_2)
                            my_calc.say_state()
                            break
                    except ArithmeticError:
                        print("The value of b can't be 0")
                    break
                elif action == '3':
                    input_string_1 = input('Enter elements of a list separated by space ')
                    print("\n")
                    input_string_2 = input('Enter elements of a list separated by space ')

                    my_calc.mulw(input_string_1, input_string_2)
                    my_calc.say_state()
                    break
                elif action == '2':
                    input_string_1 = input('Enter elements of a list separated by space ')
                    print("\n")
                    user_list1 = input_string_1.split()
                    my_calc.subi(user_list1)
                    my_calc.say_state()
                    break
                elif action == "1":
                    input_string_1 = input('Enter elements of a list separated by space ')
                    print("\n")
                    user_list1 = input_string_1.split()
                    my_calc.add(user_list1)
                    my_calc.say_state()
                    break
                elif action == "5":
                    print("Choose which function you want to execute. [1] Sine, [2] Cos ")
                    choices = input("Enter value: ")
                    if choices == "1":
                        input_value = int(input("Kindly enter the value:"))
                        print('\n')
                        my_calc.sine(input_value)
                        my_calc.say_state()
                        break
                    else:
                        input_value = int(input("Kindly enter the value:"))
                        print('\n')
                        my_calc.cose(input_value)
                        my_calc.say_state()
                        break
                elif action == "6":
                    input_string = int(input("Kindly enter number whose factorial is to be found: "))
                    if input_string < 0:
                        print("Sorry, factorial does not exist for negative numbers")
                    elif input_string == 0:
                        print("The factorial of 0 is 1")
                    else:
                        my_calc.fact(input_string)
                        my_calc.say_state()
                    break
                else:
                    print("This is fun")
        except ValueError:
            print("The choice doesnt exist. Try again with right choice")
            break

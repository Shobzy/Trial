from srcfile import Calculator


def test_add_1():
    calc = Calculator()
    calc.add([6.0, 3.0])
    assert calc.ans == 9.0


def test_add_2():
    calc = Calculator()
    calc.add([6.0, 3.0])
    assert calc.ans == 9


def test_add_3():
    calc = Calculator()
    calc.add([-6.0, 3.0])
    assert calc.ans == -3


def test_subi_1():
    calc = Calculator()
    calc.subi([6.0, 3.0])
    assert calc.ans == 3.0


def test_subi_2():
    calc = Calculator()
    calc.subi([6.0, 3.0])
    assert calc.ans == 3


def test_subi_3():
    calc = Calculator()
    calc.subi([-6.0, 3.0])
    assert calc.ans == -3


def test_div_1():
    car = Calculator()
    car.div(6.0, 3.0)
    assert car.ans == 2


def test_div_2():
    car = Calculator()
    car.div(6.0, 3.0)
    assert car.ans == 2.0


def test_div_3():
    car = Calculator()
    try:
        car.div(10, 0)
    except(ArithmeticError, IOError):
        print('\n')
        print("Arithmetic Exception")
    else:
        print("Successfully Done")


def test_div_4():
    car = Calculator()
    car.div(6.0, 3.0)
    assert car.ans == 7

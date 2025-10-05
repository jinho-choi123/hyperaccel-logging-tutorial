from ha_hello.lib.calculator import Calculator


def test_calculator_init():
    calculator = Calculator()
    assert calculator is not None


def test_calculator_add(capsys):
    calculator = Calculator()
    result = calculator.add(1, 2)
    assert result == 3


def test_calculator_subtract(capsys):
    calculator = Calculator()
    result = calculator.subtract(1, 2)
    assert result == -1


def test_calculator_multiply(capsys):
    calculator = Calculator()
    result = calculator.multiply(1, 2)
    assert result == 2


def test_calculator_divide(capsys):
    calculator = Calculator()
    result = calculator.divide(6, 2)
    assert result == 3

from src import math_func
import pytest


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    print("esta es mi primera prueba unitaria")


@pytest.mark.strings
def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Hello" in result

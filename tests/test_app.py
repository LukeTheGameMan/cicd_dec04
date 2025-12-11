import sys, pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mult, div, log, square, sin, cos, sqrt, perc

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub1():
    assert sub(4, 3) == 1

def test_sub2():
    assert sub(4, 3) != 2

def test_mult1():
    assert mult(5, 4) == 20

def test_mult2():
    assert mult(5, 4) != 21

def test_div1():
    assert div(10, 2) == 5

def test_div2():
    assert div(10, 2) != 4

def test_div3():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

def test_log1():
    assert log(10, 10) == 1

def test_log2():
    assert log(10, 10) != 0

def test_log3():
    with pytest.raises(Exception):
        log(-2, 0)

def test_square1():
    assert square(3) == 9

def test_square2():
    assert square(3) != 10

def test_sin1():
    assert sin((math.pi)/2) == 1

def test_sin2():
    assert sin(90, True) == 1

def test_sin3():
    assert sin((math.pi)/2) != 0

def test_sin4():
    assert sin(90, True) != 0

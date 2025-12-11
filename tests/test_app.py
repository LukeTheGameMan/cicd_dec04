import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, div

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub1():
    assert sub(4, 3) == 1

def test_sub2():
    assert sub(4, 3) != 2

def test_div1():
    assert div(10, 2) == 5

def test_div2():
    assert div(10, 0) != 5

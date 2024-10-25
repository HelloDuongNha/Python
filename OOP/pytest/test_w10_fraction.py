from w10_fraction import Fraction 
import pytest

def test_fraction_01(capsys):
    f = Fraction(1, 2)
    f.show()

    captured = capsys.readouterr()
    assert captured.out == '1/2'

#-1 2 
def test_fraction_02(capsys):
    f = Fraction(-1, 2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '-1/2'

#do the same for a = 1 b = -2 
def test_fraction_03(capsys):
    f = Fraction(1, -2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '-1/2'

#now -1 -2
def test_fraction_04(capsys):
    f = Fraction(-1, -2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '1/2'

#0 2 
def test_fraction_05(capsys):
    f = Fraction(0, 2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '0/2'

#0 -2 
def test_fraction_06(capsys):
    f = Fraction(0, -2)
    f.show()
    captured = capsys.readouterr()
    assert captured.out == '0/2'

#2 0 
# def test_fraction_07(capsys):
#     with pytest.raises(ZeroDivisionError):
#         f = Fraction(2, 0)
#         f.show()
#         capture = capsys.readouterr()
#         assert capture.out == "Error: Division by zero"


def test_fraction_07(capsys):
    try: 
        f = Fraction(2, 0)
        assert False 
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero'
    except Exception:
        assert False 

#-2 0
def test_fraction_08(capsys):
    try:
        f = Fraction(-2, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero'
    except Exception:
        assert False

def test_fraction_09(capsys):
    try:
        f = Fraction(0, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero'
    except Exception:
        assert False
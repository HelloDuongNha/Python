from my_function import add, my_sum

def test_add_01():
    a = -3
    b = -5
    c = -8
    assert c == add(a, b)
    
def test_add_02():
    a = 3
    b = 5
    c = 8
    assert c == add(a, b)
def test_add_03():
    a = -3
    b = 5
    c = 2
    assert c == add(a, b)
def test_add_04():
    a = 3
    b = -5
    c = -2
    assert c == add(a, b)
def test_add_05():
    a = 0
    b = 5
    c = 5
    assert c == add(a, b)
def test_add_06():
    a = 3
    b = 0
    c = 3
    assert c == add(a, b)
def test_add_07():
    a = 0
    b = -5
    c = -5
    assert c == add(a, b)
def test_add_08():
    a = -3
    b = 0
    c = -3
    assert c == add(a, b)
def test_add_09():
    a = 0
    b = 0
    c = 0
    assert c == add(a, b)

def test_sum_01():
    n = 0
    s = 0
    assert s == my_sum(n)

def test_sum_02():
    n = 5
    s = 15
    assert s == my_sum(n)

def test_sum_03():
    n = -5
    s = -15
    assert s == my_sum(n)
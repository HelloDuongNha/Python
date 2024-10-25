from w10_function import hello

#  capsys = capture system output/error
def test_hello(capsys):
    hello("Alice", 25)
    captured = capsys.readouterr()
    assert captured.out == f"Hello, my name is Alice and I am 25 years old.\n"
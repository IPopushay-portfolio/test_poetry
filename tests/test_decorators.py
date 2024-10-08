from time import sleep

from src.decorators import log


@log(filename="mylog.txt")
def test_function_success(x, y):
    sleep(5)
    return x + y


def test_log_success(capsys):
    result = test_function_success(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "test_function_success ok\nTime for work: 5\n"


@log(filename="mylog.txt")
def test_function_error(x, y):
    raise ValueError("Test error")


def test_log_error(capsys):
    result = test_function_error(1, "2")
    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "test_function_error error\n"


@log(filename="mylog.txt")
def test_log_console(capsys):
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ""  # f'{func.__name__} error: {e}. Input: {args}, {kwargs}'

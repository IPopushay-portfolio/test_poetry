from src.decorators import log


def test_log_console(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, 3)
    captured = capsys.readouterr()
    assert captured.out == ""  # f'{func.__name__} error: {e}. Input: {args}, {kwargs}'

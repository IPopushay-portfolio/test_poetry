from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Any:
    """Декоратор,который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Input: {args}, {kwargs}")

            return result

        return wrapper

    return decorator

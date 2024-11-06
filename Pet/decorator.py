import requests

def print_status_code(func):
    def jopper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, requests.Response):
            print(f"Статус код: {result.status_code}")
        elif isinstance(result, tuple) and len(result) == 2:
            # Если результат - это кортеж с двумя значениями (например, json и status_code)
            status_code = result[1]
            print(f"Статус код ответа: {status_code}")
        else:
            print(f"Функция не вернула объект Response. Статус код: Unknown")
        return result
    return jopper
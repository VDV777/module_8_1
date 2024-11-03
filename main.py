# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
#
# Пример кода:
# print(add_everything_up(123.456, 'строка'))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))

def add_everything_up(a: int | float | str, b: int | float | str) -> str:

    result = None

    try:

        result = a + b

    except Exception as e:

        print(e)

    finally:

        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
        else:
            result = a.__str__() + b.__str__()

    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print(add_everything_up(123.456, 5))
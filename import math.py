import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Корень из отрицательного числа невозможен")
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        raise ValueError("Факториал отрицательного числа невозможен")
    result = 1
    for i in range(1, a+1):
        result *= i
    return result

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

# Пример использования функций

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("Сумма:", add(a, b))
    print("Разность:", subtract(a, b))
    print("Произведение:", multiply(a, b))
    print("Частное:", divide(a, b))
    print("Возведение в степень:", power(a, b))
    print("Квадратный корень первого числа:", square_root(a))
    print("Факториал первого числа:", factorial(int(a)))
    print("Синус первого числа:", sin(a))
    print("Косинус первого числа:", cos(a))
    print("Тангенс первого числа:", tan(a))

except ValueError as e:
    print("Ошибка:", e)
except Exception as e:
    print("Произошла ошибка:", e)

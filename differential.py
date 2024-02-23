import numpy as np
import matplotlib.pyplot as plt

# Запрашиваем у пользователя значения параметров
x0 = float(input(" x: "))
y0 = float(input(" y: "))
h = float(input("integral : "))
x_max = float(input("finish x: "))

# Определяем дифференциальное уравнение
def f(x, y):
    return -y

# Создаем массив для хранения значений x и y
x_values = [x0]
y_values = [y0]

# Интегрируем дифференциальное уравнение методом Эйлера
while x0 < x_max:
    y0 += h * f(x0, y0)
    x0 += h
    x_values.append(x0)
    y_values.append(y0)

# Строим график решения
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('differential answer ')
plt.show()


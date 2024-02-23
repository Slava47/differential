import numpy as np
import matplotlib.pyplot as plt

# ����������� � ������������ �������� ����������
x0 = float(input(" x: "))
y0 = float(input(" y: "))
h = float(input("integral : "))
x_max = float(input("finish x: "))

# ���������� ���������������� ���������
def f(x, y):
    return -y

# ������� ������ ��� �������� �������� x � y
x_values = [x0]
y_values = [y0]

# ����������� ���������������� ��������� ������� ������
while x0 < x_max:
    y0 += h * f(x0, y0)
    x0 += h
    x_values.append(x0)
    y_values.append(y0)

# ������ ������ �������
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('differential answer ')
plt.show()


import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import math
from fractions import Fraction
from scipy import constants

print('Введіть множник N перед числом pi для кута -> N * pi у форматі 1/6, 0.55, 2/3 (формат модуля Fractions для '
      'рядків)')
# 'Enter the factor N before the number pi for the angle -> N * pi in the format 1/6, 0.55, 2/3 (Format of the Fractions
# module for strings)'

print('Введіть кут менший за 2/5 * pi, щоб всі кути на графіку були у одній чверті')
# Enter an angle less than 2/5 * pi so that all angles on the graph are in the same quarter

angle = Fraction(input())  # Введення значення кута в дробовому форматі за допомогою модуля fractions
print('Введіть значення швидкості м/с - формат float')
# Enter the speed value in m/s - float

velocity = float(input())  # Введення бажаної швидкості руху об'єктів

fig, ax = plt.subplots()

g = constants.g  # Отримання точного значення прискорення вільного падіння за допомогою SciPy constants

angles = [angle, angle * Fraction('3/4'), angle * Fraction('5/4')]
# Створення списку з різними значеннями кутів (За вимогами завдання)

v_x = [velocity * math.cos(i * math.pi) for i in angles]
v_y = [velocity * math.sin(i * math.pi) for i in angles]
# списки проекцій швидкостей руху на вісі відповідно до 3-х різних кутів.

length = [(velocity ** 2 * math.sin(2 * i * math.pi)) / g for i in angles]
# Обчислення значення дальності польоту для кожного з кутів

time = [length[i] / v_x[i] for i in range(3)]
# Обрахування часу польоту

time_points = [np.linspace(0, i, 100) for i in time]
# Список зі значеннями часу для кожного тіла (значення часу розбите на 100 точок починаючи від 0)

x_point = np.linspace(0, length[0], 100)
# Значення координат x (розбиття дальності польоту на 100 точок)
y_point = list((map(lambda t: v_y[0] * t - (g * t ** 2) / 2, time_points[0])))
# Обчислення значень координати у через формулу, записану у лямбда-функцію, і застосовану за допомогою функції map до
# кожного елементу списку з відповідними значеннями часу

x_point_2 = np.linspace(0, length[1], 100)
y_point_2 = list((map(lambda t: v_y[1] * t - (g * t ** 2) / 2, time_points[1])))

x_point_3 = np.linspace(0, length[2], 100)
y_point_3 = list((map(lambda t: v_y[2] * t - (g * t ** 2) / 2, time_points[2])))

line_3 = plt.plot(x_point_3, y_point_3, 'c--', label=f'Дальність польоту приблизо {round(length[2], 2)} м.')
line = plt.plot(x_point, y_point, 'g--', label=f'Дальність польоту приблизо {round(length[0], 2)} м.')
line_2 = plt.plot(x_point_2, y_point_2, 'b--', label=f'Дальність польоту приблизо {round(length[1], 2)} м.')
# Побудова кривих, що відповідають траєкторіям польоту

plt.axis([0, math.ceil(max(length)), 0, math.ceil(max(y_point_3))])
# Побудова осей координат з довжиною відповідною до максимальних значень координат.

redDot, = plt.plot([0], [0], 'ro')
cyanDot, = plt.plot([0], [0], 'co')
magentaDot, = plt.plot([0], [0], 'mo')
# Створення трьох точок різного кольору розташованих у початку координат


def animate(i, x, y, x_2, y_2, x_3, y_3):
    redDot.set_data(x[i], y[i])
    cyanDot.set_data(x_2[i], y_2[i])
    magentaDot.set_data(x_3[i], y_3[i])
    return redDot, cyanDot, magentaDot,
# Функція анімації, що відповідно до номеру ітерації i передає кожній точці нові значення координат


myAnimation = animation.FuncAnimation(fig, animate, frames=len(time_points[0]),
                                      fargs=(x_point, y_point, x_point_2, y_point_2, x_point_3, y_point_3), interval=10,
                                      blit=True, repeat=True)
# Створення анімації за допомогою FuncAnimation

plt.xlabel('x')
plt.ylabel('y')
plt.title('Показано траєкторії для кутів 3/4, 1 і 5/4 від заданого')
plt.legend()
plt.show()
# Виведення графіка на екран.

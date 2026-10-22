import tkinter as tk
from tkinter import Canvas, colorchooser, LEFT, TOP, BOTTOM, RIGHT

master = tk.Tk()
canvas = tk.Canvas(master, width=800, height=600, background='#FFFFFF')

# Глобальные переменные
point_count = 0

# Вспомогательная функция для реализации аналога команды PSet
def _create_point(self, x, y, point_color='#000000', line_width=1, **kwargs):
    return self.create_oval(x - line_width / 2, y - line_width / 2,
                            x + line_width / 2, y + line_width / 2,
                            fill=point_color, outline=point_color,
                            **kwargs)
tk.Canvas.create_point = _create_point


'''
' ЗАДАНИЕ 1:
'    Просто запустить эту процедуру. Увидеть СТУПЕНЧАТОСТЬ отрисовки линии.
' Затем внимательно изучить данную процедуру. Вспомнить, что рисование в машинной графике - это рисование
' по сетке пикселов.
'    В данной процедуре реализован пошаговый алгоритм рисования отрезка, когда угол наклона
' к оси OX меньше 45 градусов.
'
'''
def LineAngleBelow45Deg():
    global point_count
    # Начальная точка отрезка
    start_x = 10
    start_y = 10
    canvas.create_point(start_x, start_y, '#FF0000', line_width=4)
    # Конечная точка отрезка
    end_x = 500
    end_y = 40
    canvas.create_point(end_x, end_y, '#FF0000', line_width=4)
    # Поточечно рисуем отрезок между точками с координатами
    # (start_x, start_y) и (end_x, end_y)
    for delta_x in range(end_x - start_x):
        current_x = start_x + delta_x
        current_y = start_y + (end_y - start_y) * (current_x - start_x) / (end_x - start_x)
        canvas.create_point(current_x, round(current_y), '#FF0000')
        point_count += 1
    lbl_point_num.configure(text=str(point_count))


'''
' ЗАДАНИЕ 2:
'    Написать процедуру "поточечного" (пошагового) построения отрезка, угол наклона которого к оси ОХ равен 45 градусам.
' Для этого необходимо задать координаты конечной точки отрезка (end_x, end_y) так,
' чтобы отрезок был нарисован под углом 45 градусов.
'    Запустить эту процедуру. Убедиться в правильности выбранных координат end_x, end_y (выбор ведь не единственный?).
' Увидеть, что ступенька в этом случае равна одному пикселу - линия идеальна (так же как в случае строго горизонтальной и
' вертикальной линий).
'
'''
def LineAngleEqual45Deg():
    pass


'''
' ЗАДАНИЕ 3:
'    Запустить эту процедуру, в которой воплощён пошаговый алгоритм рисования отрезка, угол наклона которого
' к оси OX больше 45 градусов. Увидеть, что цикл по X рисует не сплошную линию, так как
' при угле наклона больше 45 градусов приращение по оси X на один пиксел даёт большой скачок по оси Y.
'    Исправить зависимость линейной функции таким образом, чтобы получилась
' "правильная сплошная линия".
' (Вопрос: "Как исправить?" Обычно ответ:
' "Уменьшить шаг". Проверяем и убеждаемся, что не получаем нужного результата.
' Надо догадаться, что рисовать надо зависимость X=f(Y), а не Y=f(X), как
' в предыдущих случаях.
'''
def LineAngleAbove45Deg():
    global point_count
    # Начальная точка отрезка
    start_x = 10
    start_y = 10
    canvas.create_point(start_x, start_y, '#FF00FF', line_width=4)
    # Конечная точка отрезка
    end_x = 20
    end_y = 550
    canvas.create_point(end_x, end_y, '#FF00FF', line_width=4)
    # Поточечно рисуем отрезок между точками с координатами
    # (start_x, start_y) и (end_x, end_y)
    # Здесь цикл идёт по Y, потому что угол > 45°
    for delta_x in range(end_x - start_x):
        current_x = start_x + delta_x
        current_y = start_y + (end_y - start_y) * (current_x - start_x) / (end_x - start_x)
        canvas.create_point(current_x, round(current_y), "#F700FF")
        point_count += 1
    lbl_point_num.configure(text=str(point_count))


'''
' ЗАДАНИЕ 4:
'    Используя уравнение окружности X^2 + Y^2 = R^2 (центр в т.(0,0)),
' написать цикл пошагового рисования окружности. Запустить эту процедуру.
'
' Пусть радиус рисуемой окружности равен 100.
'''
def PointCircle():
    global point_count

    lbl_point_num.configure(text=str(point_count))


'''
' ЗАДАНИЕ 5:
'    Выведите функцию y=f(x) для окружности, центр которой не лежит в т.(0,0), а находится ~ в центре экрана
' или просто в видимой области экрана. Используя полученное уравнение окружности,
' напишите цикл пошагового рисования окружности. Запустите эту процедуру.
'
' Пусть радиус рисуемой окружности равен 100.
'''
def PointMidCircle():
    global point_count

    lbl_point_num.configure(text=str(point_count))


# Очистка экрана
def CleanScreen():
    global point_count
    canvas.delete("all")
    point_count = 0
    lbl_point_num.configure(text=str(point_count))


# ЗАГОТОВКА ФОРМЫ
frame_top = tk.Frame(master)
btn_line_below_45 = tk.Button(frame_top, text='Отрезок (<45)',
                              command=LineAngleBelow45Deg)
btn_line_equal_45 = tk.Button(frame_top, text='Отрезок (=45)',
                              command=LineAngleEqual45Deg)
btn_line_above_45 = tk.Button(frame_top, text='Отрезок (>45)',
                              command=LineAngleAbove45Deg)
btn_circle = tk.Button(frame_top, text='Окружность',
                       command=PointCircle)
btn_mid_circle = tk.Button(frame_top, text='Окружность (центр)',
                           command=PointMidCircle)

frame_top.pack(side=TOP)
btn_line_below_45.pack(side=LEFT)
btn_line_equal_45.pack(side=LEFT)
btn_line_above_45.pack(side=LEFT)
btn_circle.pack(side=LEFT)
btn_mid_circle.pack(side=LEFT)


frame_bottom = tk.Frame(master)
lbl_points = tk.Label(frame_bottom, text='Кол-во точек:')
lbl_point_num = tk.Label(frame_bottom, text=str(point_count))
btn_clean = tk.Button(frame_bottom, text='Очистить экран',
                      command=CleanScreen)
frame_bottom.pack(side=BOTTOM)
lbl_points.pack(side=LEFT)
lbl_point_num.pack(side=LEFT)
btn_clean.pack(side=LEFT)

canvas.pack()
master.mainloop()

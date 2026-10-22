'''
' Лаб.раб.№6 "Вычисление площади и периметра произвольного многоугольника методом трапеции"

' ПОСТАНОВКА ЗАДАЧИ. Имеется произвольный замкнутый контур. Рассчитать площадь внутри
' заданного контура и периметр контура.

' РЕШЕНИЕ. "Обкалываем" контур точками. Эти точки станут вершинами вписанного многоугольника.
' Так как для хранения координат точек используется массив с динамически изменяющейся
' верхней границей, то количество точек может быть произвольным. Чаще "обкололи" -
' точнее совпадет площадь вписанного многоугольника (с вершинами в этих точках) с
' площадью внутри контура.

' ПРИМЕЧАНИЕ. Сравнить результаты расчетов со всех компьютеров - они должны быть близки
' несмотря на различным образом поставленные точки.
'''

import tkinter as tk
from tkinter import Canvas, LEFT, TOP, BOTTOM, RIGHT

master = tk.Tk()
master.title('Лаб.раб.№6 — Площадь и периметр многоугольника методом трапеций')
w = tk.Canvas(master, width=800, height=600, background='#FFFFFF')

# Переменные программы
Drawing = False
Color = '#FF00FF'

XX = []
YY = []
N = 0
K = 0

StatusCoord = ''

# высота трапеции
h = 0
# 1-ое основание трапеции
a = 0
# 2-ое основание трапеции
b = 0

# переменная для суммы площадей всех трапеций кроме замыкающей
S_wo_closeTr = 0.0
# переменная для площади замыкающей трапеции
S_closeTr = 0.0
# переменная для площади многоугольника
S_Poly = 0.0
# переменная для периметра
P = 0.0

txtS1 = tk.StringVar()
txtS2 = tk.StringVar()
txtS3 = tk.StringVar()
txtP = tk.StringVar()

# Вспомогательная функция для реализации аналога команды PSet
def _create_point(self, x, y, pointColor='#000000', lineWidth=1, **kwargs):
    return self.create_oval(x-lineWidth/2, y-lineWidth/2,
                            x+lineWidth/2, y+lineWidth/2,
                            fill=pointColor, outline=pointColor,
                            **kwargs)
tk.Canvas.create_point = _create_point

# Событие MouseDown (мышь вниз) — ставим точки
def MouseDownLB(event):
    global Drawing
    global N
    DrawWidth = 3
    Drawing = True
    CurrentX = event.x
    CurrentY = event.y
    w.create_point(event.x, event.y, Color, DrawWidth)
    XX.append(CurrentX)
    YY.append(CurrentY)
    w.create_text(XX[N], YY[N], anchor=tk.NW,
                  text=str(N) + ' (' + str(XX[N]) + ',' + str(YY[N]) + ')')
    N += 1
w.bind('<Button-1>', MouseDownLB)

def Polygon_Click():
    DrawWidth = 1
    # Нарисуем ось X
    w.create_line(0, 2, 700, 2, width=DrawWidth, fill='#000000')
    # Рисуем стороны многоугольника
    for K in range(N-1):
        w.create_line(XX[K], YY[K], XX[K+1], YY[K+1], width=DrawWidth, fill=Color)
    # Задание 1: Рисуем замыкающую сторону многоугольника


def Normal_Click():
    DrawWidth = 1
    for K in range(N):
        pass
        #Задание 2: Опускаем перпендикуляры на ось Х из вершин многоугольника


# ========== РАСЧЁТЫ + ВИЗУАЛИЗАЦИЯ ==========

'''
'Задание 3: Подсчет суммы площадей трапеций (кроме последней трапеции) с использованием
'           формулы площади трапеции
'''

def AreaAllTrap():
    global h, a, b, S_wo_closeTr
    w.delete('trap')
    S_wo_closeTr = 0.0
    for K in range(N-1):
        pass
        # Высота

        # Основание 1

        # Основание 2

        # Площадь
        


        # Цвет по знаку вклада
        fill_color = '#90EE90' if s >= 0 else '#FFB6C1'
        outline_color = '#006400' if s >= 0 else '#8B0000'

        w.create_polygon(
            XX[K], 0,
            XX[K], YY[K],
            XX[K+1], YY[K+1],
            XX[K+1], 0,
            fill=fill_color, outline=outline_color, width=1, tags='trap'
        )

        mid_x = (XX[K] + XX[K+1]) / 2
        mid_y = max(15, (YY[K] + YY[K+1]) / 4)
        w.create_text(mid_x, mid_y, text=f'{s:.1f}',
                      fill='#000000', font=('Arial', 8, 'bold'), tags='trap')

    w.tag_lower('trap')
    txtS1.set(f'{abs(S_wo_closeTr):.2f}')

'''
 'Задание 4: Подсчёт последней "замыкающей" площади
'''
def AreaCloseTrap():
    global h, a, b, S_closeTr
    if N < 2:
        return


    fill_color = '#87CEEB'
    outline_color = '#00008B'

    w.create_polygon(
        XX[N-1], 0,
        XX[N-1], YY[N-1],
        XX[0], YY[0],
        XX[0], 0,
        fill=fill_color, outline=outline_color, width=2, tags='trap'
    )

    mid_x = (XX[N-1] + XX[0]) / 2
    mid_y = max(15, (YY[N-1] + YY[0]) / 4)
    w.create_text(mid_x, mid_y, text=f'{S_closeTr:.1f} (замык.)',
                  fill='#00008B', font=('Arial', 8, 'bold'), tags='trap')

    w.tag_lower('trap')
    txtS2.set(f'{abs(S_closeTr):.2f}')

'''
' Задание 5: Получение окончательной величины площади S_мноуголника:
'''
def AreaPolygon():
    global S_Poly



    txtS3.set(f'{abs(S_Poly):.2f}')

    if N >= 3:
        coords = []
        for i in range(N):
            coords.extend([XX[i], YY[i]])
        w.delete('polyfill')
        w.create_polygon(coords, fill='#E6E6FA', outline='',
                         stipple='gray50', tags='polyfill')
        w.tag_lower('polyfill')

'''
' Задание 6: Вычислить периметр многоугольника.
' При подсчете периметра используем формулу из лекций и
' фрагменты процедур расчета площади
'''

def PerimeterPolygon():
    global P
    P = 0.0




    txtP.set(f'{P:.2f}')

# Событие MouseUp
def MouseUpLB(event):
    global Drawing
    Drawing = False
master.bind('<ButtonRelease-1>', MouseUpLB)

def MouseMoveCoord(event):
    global StatusCoord
    StatusCoord = "Координаты: X = " + str(event.x) + ", Y = " + str(event.y)
    txtCoord.configure(text=StatusCoord)
w.bind('<Motion>', MouseMoveCoord)

# Очистка / Сброс
def CleanScreen_Click():
    global XX, YY, N, K, h, a, b
    global S_wo_closeTr, S_closeTr, S_Poly, P

    w.delete('all')

    XX = []
    YY = []
    N = 0
    K = 0

    h = 0
    a = 0
    b = 0

    S_wo_closeTr = 0.0
    S_closeTr = 0.0
    S_Poly = 0.0
    P = 0.0

    txtS1.set('')
    txtS2.set('')
    txtS3.set('')
    txtP.set('')

# ==================== ИНТЕРФЕЙС ====================

# Верхняя панель: рисование + сброс
fr_top = tk.Frame(master, pady=4)
fr_top.pack(side=TOP, fill=tk.X)

btnPolygon = tk.Button(fr_top, text='Нарисовать стороны\nмногоугольника',
                       width=18, height=3, command=Polygon_Click)
btnNormal  = tk.Button(fr_top, text='Нарисовать перпендикуляры\nиз вершин на ось Ox',
                       width=22, height=3, command=Normal_Click)
btnReset   = tk.Button(fr_top, text='Сброс',
                       width=10, height=3, bg='#FFCCCC',
                       command=CleanScreen_Click)

btnPolygon.pack(side=LEFT, padx=4, pady=2)
btnNormal.pack(side=LEFT, padx=4, pady=2)
btnReset.pack(side=LEFT, padx=12, pady=2)

# Панель расчётов
fr_calc = tk.Frame(master, pady=6)
fr_calc.pack(side=TOP, fill=tk.X)

btn_opts = {'width': 16, 'height': 3, 'wraplength': 120}
ent_opts = {'width': 14, 'justify': 'center'}

# Колонка 1
fr1 = tk.Frame(fr_calc, padx=6)
fr1.pack(side=LEFT)
btnAreaAllTrap = tk.Button(fr1, text='Сумма площадей\nвсех трапеций,\nкроме замыкающей',
                           command=AreaAllTrap, **btn_opts)
Text1 = tk.Entry(fr1, textvariable=txtS1, **ent_opts)
btnAreaAllTrap.pack(pady=(0, 2))
Text1.pack()

# Колонка 2
fr2 = tk.Frame(fr_calc, padx=6)
fr2.pack(side=LEFT)
btnAreaCloseTrap = tk.Button(fr2, text='Площадь\nзамыкающей\nтрапеции',
                             command=AreaCloseTrap, **btn_opts)
Text2 = tk.Entry(fr2, textvariable=txtS2, **ent_opts)
btnAreaCloseTrap.pack(pady=(0, 2))
Text2.pack()

# Колонка 3
fr3 = tk.Frame(fr_calc, padx=6)
fr3.pack(side=LEFT)
btnAreaPolygon = tk.Button(fr3, text='Площадь\nмногоугольника',
                           command=AreaPolygon, **btn_opts)
Text3 = tk.Entry(fr3, textvariable=txtS3, **ent_opts)
btnAreaPolygon.pack(pady=(0, 2))
Text3.pack()

# Колонка 4
fr4 = tk.Frame(fr_calc, padx=6)
fr4.pack(side=LEFT)
btnPerimeterPolygon = tk.Button(fr4, text='Периметр\nмногоугольника',
                                command=PerimeterPolygon, **btn_opts)
Text5 = tk.Entry(fr4, textvariable=txtP, **ent_opts)
btnPerimeterPolygon.pack(pady=(0, 2))
Text5.pack()

# Нижняя панель — координаты
fr_bottom = tk.Frame(master, pady=4)
fr_bottom.pack(side=BOTTOM, fill=tk.X)
txtCoord = tk.Label(fr_bottom, text=StatusCoord, font=('Arial', 9))
txtCoord.pack()

# Холст
w.pack(fill=tk.BOTH, expand=True)

master.mainloop()

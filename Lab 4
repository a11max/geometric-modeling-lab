import tkinter as tk
from tkinter import Canvas, LEFT, TOP, BOTTOM, RIGHT

master = tk.Tk()
w = tk.Canvas(master, width=800, height=600, background='#FFFFFF')

# Переменные программы
Drawing = False
CurveDrawn = False

TangentColor = '#000000'
ContourColor = '#FF00FF'
BezierColor = '#0000FF'
BackColor = '#FFFFFF'

N = 0

X_p = 250.0
Y_p = 250.0
X_p1 = 0.0
Y_p1 = 0.0
XX = []
YY = []

# Вспомогательная функция для реализации аналога команды PSet
def _create_point(self, x, y, pointColor='#000000', lineWidth=1, **kwargs):
    return self.create_oval(x-lineWidth/2, y-lineWidth/2, 
                            x+lineWidth/2, y+lineWidth/2, 
                            fill=pointColor,outline=pointColor,
                            **kwargs)
tk.Canvas.create_point = _create_point

'''
'ЗАДАНИЕ 0. Алгоритм Брезенхейма
'''

def LineAngleBelow45Deg():
    # Начальная и конечная точки (пологий отрезок)
    x_start, y_start = 10, 10
    x_finish, y_finish = 500, 12

    delta_x = x_finish - x_start
    delta_y = y_finish - y_start

    error = 0

    delta_err = delta_y + 1

    y_current = y_start

    for x_current in range(x_start, x_finish + 1):
        w.create_point(x_current, y_current, '#FF0000', 1)
        error += delta_err
        if error >= (delta_x + 1):
            pass
            #Спускаемся вниз на одну строчку
            #Обнуляем ошибку или вычитаем дельту x

# Метки точек
P0 = tk.Label(w, text='P0')
P1 = tk.Label(w, text='P1')
P2 = tk.Label(w, text='P2')
P3 = tk.Label(w, text='P3')

#P0.place(x=20,y=20)
#P1.place(x=20,y=20)
#P2.place(x=20,y=20)
#P3.place(x=20,y=20)

'''
'ЗАДАНИЕ 1. Рисуем произвольно расположенные 4 точки
'''
# Событие MouseDown(Мышь вниз)
def MouseDownLB(event):
    global N
    global Drawing
    DrawWidth = 4
    Drawing = True
    # 'При нажатии левой клавиши мыши ставим точку. Её координаты обозначим (X_точки,Y_точки)
    #'Т.о. текущие X-координата и Y-координата мыши(Current -текущий) станут координатами
    #'очередной из точек P0, P1, P2, P3.
    CurrentX = event.x
    CurrentY = event.y
    # Ограничение N < 4 не позволяет нарисовать больше 4-ёх точек (нам больше и не нужно).
    if N < 4:
        XX.append(CurrentX)
        YY.append(CurrentY)
        # В том месте формы, где щелкнули мышью, появится очередная из точек P0,P1,P2,P3.
        w.create_point(event.x, event.y, ContourColor, DrawWidth)
        N += 1
w.bind('<Button-1>', MouseDownLB)

# Событие MouseUp(Мышь вверх)
def MouseUpLB(event):
    global Drawing
    w.old_coords = None
    Drawing = False

master.bind('<ButtonRelease-1>', MouseUpLB)

'''
'ЗАДАНИЕ 2. Нарисовать замкнутый контур с вершинами в этих 4-х точках.
'Две стороны этого контура - касательные, на которых будет построена кривая Безье.
'''
def Contour_Click():
    try:
        DrawWidth = 1
        #'Из точки P0 в P1:
        w.create_line(XX[0],YY[0],XX[1],YY[1], width=DrawWidth, fill=TangentColor)
        #'Из точки P1 в P2:
        w.create_line(XX[1],YY[1],XX[2],YY[2], width=DrawWidth, fill=ContourColor)
        #'Из точки P2 в P3:

        #'Из точки P3 в P0:

        '''
        ' Назовем полученные 4 точки P0, P1, P2, P3. Для этого разместим
        ' метки на форме у соответствующих точек. Учтем, что,например,
        ' Х-координата метки P0 - это свойство Left, Y-координата - это свойство Top.
        ' Например, запись P0.Left = 100 означает, что Х-координата метки P0 равна 50.
        ' В tkcanvas в качестве меток используем виджеты Label (см. выше)
        '''
        # Устанавливаем метку P0
        P0.place(x=XX[0],y=YY[0])
        # Устанавливаем метку P1

        # Устанавливаем метку P2

        # Устанавливаем метку P3

    except:
        print ('ОШИБКА: Точки не расставлены!')
		
'''
'ЗАДАНИЕ 3. Построить кривую Безье по полученным касательным.
'''
def Bezier_Click():
    global CurveDrawn
    try:
        DrawWidth = 2
        for uv in range(1001):
            u = uv / 1000

            w.create_point(X, Y, BezierColor, DrawWidth)
        CurveDrawn = True
    except:
        print ('ОШИБКА: Точки не расставлены!')
		
def Hermite_Click():
    global CurveDrawn
    try:
        DrawWidth = 2
        for uv in range(1001):
            u = uv / 1000

            w.create_point(XU, YU, '#00FA00', DrawWidth)
        CurveDrawn = True
    except:
        print ('ОШИБКА: Точки не расставлены!')
		
'''
'ЗАДАНИЕ 4: Дописать процедуру MouseMove, позволяющую в динамике рисовать Кривые Безье.

'          Последовательность рисования множества Кривых Безье:
'1. Стираем стороны P0P1 и P1P2 предыдущего контура и очередную Кривую Безье
'2. Рисуем стороны P0P1 и P1P2 нового контура и новую Кривую Безье
'3. Запомнили координаты точки Р1
'  !!!!очистить данные для первого раза из прошлых процедур
'''
def MouseMove(event):
    global Drawing
    DrawWidth = 1
    Drawing = True
    '''
    if CurveDrawn:
        for uv in range(1001):
        u = uv / 1000
            X = XX[0] * (1-u)**3 + 3*XX[1]*(1-u)**2*u + 3*XX[2]*(1-u)*u**2 + XX[3]*u**3
            Y = YY[0] * (1-u)**3 + 3*YY[1]*(1-u)**2*u + 3*YY[2]*(1-u)*u**2 + YY[3]*u**3
            w.create_point(X, Y, BackColor, DrawWidth)
    else:
    '''
    CurrentX = event.x
    CurrentY = event.y
    XX[1] = CurrentX
    YY[1] = CurrentY
    # Рисуем очередную точку P1
    w.create_point(XX[0], YY[0], ContourColor, DrawWidth)


    '''
    ' 2а. Рисуем стороны  нового контура (2 стороны просто перерисовываем):
    '''
    #'Из точки P0 в P1:
    #w.create_line(XX[0],YY[0],XX[1],YY[1], width=DrawWidth, fill=TangentColor)
    #'Из точки P1 в P2:
    #w.create_line(XX[1],YY[1],XX[2],YY[2], width=DrawWidth, fill=ContourColor)
    #'Из точки P2 в P3:
    #w.create_line(XX[2],YY[2],XX[3],YY[3], width=DrawWidth, fill=TangentColor)
    #'Из точки P3 в P0:
    #w.create_line(XX[3],YY[3],XX[0],YY[0], width=DrawWidth, fill=ContourColor)
    P1.place(x=XX[1],y=YY[1])
    '''
    ' 2б.  Рисуем новую кривую Безье:
    '''
    for uv in range(1001):
        u = uv / 1000
        #X = XX[0] * (1-u)**3 + 3*XX[1]*(1-u)**2*u + 3*XX[2]*(1-u)*u**2 + XX[3]*u**3
        #Y = YY[0] * (1-u)**3 + 3*YY[1]*(1-u)**2*u + 3*YY[2]*(1-u)*u**2 + YY[3]*u**3
        #w.create_point(X, Y, BezierColor, DrawWidth)
    '''
    ' 3. Отправляем на хранение координаты новой точки P1:
    '''
    w.old_coords = XX[1],YY[1]
        
w.bind('<B1-Motion>', MouseMove)

# 'Чистим экран и массив для 4-х точек P0,P1,P2,P3
def CleanScreen_Click():
    global XX
    global YY
    global N
    w.delete('all')
    XX = []
    YY = []
    N = 0
    
    P0.place(x=20,y=20)
    P1.place(x=20,y=20)
    P2.place(x=20,y=20)
    P3.place(x=20,y=20)



# ЗАГОТОВКА ФОРМЫ
fr1 = tk.Frame(master)
btnLine45 = tk.Button(fr1, text = 'Отрезок <45°',
                          command=LineAngleBelow45Deg)
btnContour = tk.Button(fr1, text = 'Контур',
                          command=Contour_Click)
btnBezier = tk.Button(fr1, text = 'Кривая Безье',
                          command=Bezier_Click)
btnHermite = tk.Button(fr1, text = 'Кривая Эрмита',
                          command=Hermite_Click)
btnCls = tk.Button(fr1, text = 'Очистка формы', 
                          command=CleanScreen_Click)
fr1.pack(side=TOP)
btnLine45.pack(side=LEFT)
btnContour.pack(side=LEFT)
btnBezier.pack(side=LEFT)
btnHermite.pack(side=LEFT)
btnCls.pack(side=LEFT)

w.pack()
w.old_coords = None
master.mainloop()

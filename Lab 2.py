import tkinter as tk
from tkinter import Canvas, colorchooser, LEFT, TOP, BOTTOM, RIGHT

master = tk.Tk()
w = tk.Canvas(master, width=800, height=600, background='#FFFFFF')

# Переменные программы
AllowDrawing = False
DrawColor = '#000000'
BackColor = '#FFFFFF'
DrawWidth = 1

StatusCoord = ''

SHIFT_MASK = False

# ЧАСТЬ I "Установка основных параметров для рисования"
# Выберем цвет фона из палитры
def BGColor_Click():
    global BackColor
    color = colorchooser.askcolor(title ="Выбор цвета формы")
    BackColor = color[1]
    w.configure(bg=BackColor)
    #btnBGPick.configure(foreground = BackColor)
    #btnEraser.configure(foreground = BackColor)

# Выберем цвет рисования из палитры
def FGColor_Click():
    global DrawColor
    color = colorchooser.askcolor(title ="Выбор цвета формы")
    DrawColor = color[1]
    #btnFGPick.configure(foreground = DrawColor)



def Eraser_Click():
    global DrawColor
    # **Задание 1**: Впишите строку реализации ластика. Стирать ластиком означает рисование цветом фона.

    #btnFGPick.configure(foreground = DrawColor)

# Увеличить толщину рисования
def Thick_Click():
    global DrawWidth
    DrawWidth = DrawWidth + 1
    RedrawLineDemo()

# **Задание 2**: Уменьшить толщину рисования.

def Thin_Click():
    global DrawWidth
    if DrawWidth > 1:
# Напишите здесь оператор уменьшения толщины линии
        pass

    RedrawLineDemo()

# Перерисовка линии для демонстрации толщины кисти
def RedrawLineDemo():
    lineDemo.delete("all")
    lineDemo.create_line(10,10,40,40,width=DrawWidth)

# ЧАСТЬ II "Основные события мыши"
'''
Существуют 3 основных события мыши:
1. Событие MouseDown(Мышь вниз) происходит, когда нажата одна из кнопок мыши (левая или правая)
2. Событие MouseMove(Перемещение мыши) происходит, когда перемещаем указатель мыши
3. Событие MouseUp(Мышь вверх) происходит, когда отпускаем кнопку мыши
'''

# Эта процедура разрешает или запрещает рисование по щелчку
# по клавише "Разрешить/Запретить рисование мышью"
def AllowDrawing_Click():
    global AllowDrawing
    if not AllowDrawing:
        btnAllow.configure(bg='#A8EAB8')
        AllowDrawing = True
        btnAllow.configure(text='РИСОВАНИЕ? ' + str(AllowDrawing))
    else:
        btnAllow.configure(bg='#FA7C76')
        AllowDrawing = False
        btnAllow.configure(text='РИСОВАНИЕ? ' + str(AllowDrawing))

# Событие MouseDown(Мышь вниз)

# Вспомогательная функция для реализации команды Circle
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc

def MouseDownLB(event):
    w.create_circle(event.x, event.y, 10, outline="#00FF00")

def MouseDownRB(event):
    w.create_circle(event.x, event.y, 30, outline="#FFFF00")

master.bind('<Button-1>', MouseDownLB)
master.bind('<Button-3>', MouseDownRB)

# Событие MouseMove(Перемещение мыши)
def ShiftBlock(event):
    global SHIFT_MASK
    SHIFT_MASK = True
    
def ShiftRelease(event):
    global SHIFT_MASK
    SHIFT_MASK = False
    
master.bind('<Shift_L>', ShiftBlock)
master.bind('<Shift_R>', ShiftBlock)
master.bind('<KeyRelease-Shift_L>', ShiftRelease)
master.bind('<KeyRelease-Shift_R>', ShiftRelease)

# Вспомогательные функции для расчета HEX-кода цвета
def ColorRgbToHex(rgb):
    def truncColor(x):
        if x > 255:
            return 255
        elif x < 0:
            return 0
        else:
            return x
    
    R = truncColor(rgb[0])
    G = truncColor(rgb[1])
    B = truncColor(rgb[2])
    
    return '#%02x%02x%02x' % (R,G,B) 

def ColorNumToHex(num):
    if num > 16777215:
        res = 16777215
    elif num < -16777215:
        res = -16777215
    else:
        res = num
    
    if res < 0:
        return '#' + hex(num)[3:].zfill(6)
    else:
        return '#' + hex(res)[2:].zfill(6)

def MouseMoveCoord(event):    
    global StatusCoord
    StatusCoord = "Координаты: X = " + str(event.x) + ", Y = " + str(event.y)
    txtCoord.configure(text=StatusCoord)
    
def MouseMove(event):
    global StatusCoord
    global AllowDrawing
    StatusCoord = "Координаты: X = " + str(event.x) + ", Y = " + str(event.y)
    txtCoord.configure(text=StatusCoord)    
    if AllowDrawing:
        if SHIFT_MASK:
            AllowDrawing = False
            btnAllow.configure(bg='#FA7C76')
            btnAllow.configure(text='РИСОВАНИЕ? ' + str(AllowDrawing))
        else:
            x, y = event.x, event.y
            if w.old_coords:
                x1, y1 = w.old_coords
                # **Задание 3**: Создание кисти
                w.create_line(x, y, x1, y1, fill=DrawColor, width=DrawWidth)



            w.old_coords = x, y
        
master.bind('<B1-Motion>', MouseMove)
master.bind('<B3-Motion>', MouseMove)
master.bind('<Motion>', MouseMoveCoord)

# Событие MouseUp(Мышь вверх)
def MouseUpLB(event):
    global AllowDrawing
    w.old_coords = None
    # w.create_circle(event.x, event.y, 10, outline="#00FF00", fill=DrawColor)
    # AllowDrawing = False
    
def MouseUpRB(event):
    global AllowDrawing
    w.old_coords = None
    # w.create_circle(event.x, event.y, 30, outline="#FFFF00", fill=DrawColor)
    # AllowDrawing = False
    
master.bind('<ButtonRelease-1>', MouseUpLB)
master.bind('<ButtonRelease-3>', MouseUpRB)

# ЗАГОТОВКА ФОРМЫ
fr1 = tk.Frame(master)
btnAllow = tk.Button(fr1, text='РИСОВАНИЕ? ' + str(AllowDrawing),
                    background='#FA7C76',
                    command=AllowDrawing_Click)
fr1.pack()
btnAllow.pack(side=LEFT)

fr2 = tk.Frame(master)
btnBGPick = tk.Button(fr2, text='Цвет фона',
                    width=15,
                    #foreground=BackColor,
                    command=BGColor_Click)
btnFGPick = tk.Button(fr2, text='Цвет рисования',
                    #foreground=DrawColor,
                    width=15,
                    command=FGColor_Click)
btnEraser = tk.Button(fr2, text='Ластик',
                    #foreground=BackColor,
                    width=15,
                    command=Eraser_Click)
fr2.pack(side=LEFT)
btnBGPick.pack()
btnFGPick.pack()
btnEraser.pack()

fr3 = tk.Frame(master)
btnThick = tk.Button(fr3, text='+ Толщина',
                    width=15,
                    command=Thick_Click)
btnThin = tk.Button(fr3, text='- Толщина',
                    width=15,
                    command=Thin_Click)
lineDemo = tk.Canvas(fr3, width=50, height=50, background='#FFFFFF')
lineDemo.create_line(10,10,40,40,width=DrawWidth)
fr3.pack(side=RIGHT)
btnThick.pack()
btnThin.pack()
lineDemo.pack()

fr4 = tk.Frame(master)
txtCoord = tk.Label(fr4,text=StatusCoord)
fr4.pack(side=BOTTOM)
txtCoord.pack()

# ЗАПУСК ПРОГРАММЫ
w.pack()
w.old_coords = None
master.mainloop()





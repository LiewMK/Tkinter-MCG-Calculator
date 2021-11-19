from tkinter import *
import tkinter as tk
import tkinter.messagebox
import math
import winsound
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

def openvectorMenu():
    topVectorMenu = Toplevel()
    topVectorMenu.title("Vector Calculator")
    topVectorMenu.geometry("1251x703+120+50")
    root.withdraw()

    winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)

    vectorMainMenu = PhotoImage(file="vectorMainMenu.png")
    label = Label(topVectorMenu, image=vectorMainMenu)
    label.image = vectorMainMenu
    label.place(height=703, width=1251, x=0, y=0)

    def openVector2d():
        def Addition(i1, j1, i2, j2):
            ans = (round(i1 + i2, 2), round(j1 + j2, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def Subtraction(i1, j1, i2, j2):
            ans = (round(i1 - i2, 2), round(j1 - j2, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def DotProduct(i1, j1, i2, j2):
            ans = (round(i1 * i2, 2), round(j1 * j2, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def Magnitude(i1, j1):
            ans = round(((i1 ** 2 + j1 ** 2) ** (1 / 2)), 2)
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text="Magnitude (Vector A) = " + str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def FindingAngle(i1, j1, i2, j2):
            a = i1 * i2 + j1 * j2
            b = (i1 ** 2 + j1 ** 2) ** (1 / 2)
            c = (i2 ** 2 + j2 ** 2) ** (1 / 2)
            d = a / (b * c)
            ans = round(math.degrees(math.acos(d)), 2)
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text="Angle (in degree) = " + str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def UnitVector(i1, j1):
            a = (i1 ** 2 + j1 ** 2) ** (1 / 2)
            ans = (round(i1 / a, 2), round(j1 / a, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text="Unit Vector (Vector A)" + "\n""= " + str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def Orthogonality(i1, j1, i2, j2):
            a = i1 * i2 + j1 * j2
            if a == 0:
                ans = ("Perpendicular")
            elif a != 0:
                ans = ("Not perpendicular")
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def Parallelism(i1, j1, i2, j2):
            a = i1 * j2
            b = i2 * j1
            if a == b:
                ans = ("Parallel")
            elif a != b:
                ans = ("Not Parallel")
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        def delete():
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block4.delete(first=0, last=100)
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector2d, font="Tahoma 15 bold", text=" ", background="#030706")
            OutputPlace.place(height=50, width=370, x=438, y=530)

        topVector2d = Toplevel()
        topVector2d.title("2D Vector Calculator")
        topVector2d.geometry("1251x703+120+50")
        topVectorMenu.withdraw()

        winsound.PlaySound("sound1_2.wav", winsound.SND_ASYNC)

        vector2D = PhotoImage(file="vector2D.png")
        label = Label(topVector2d, image=vector2D)
        label.image = vector2D
        label.place(height=703, width=1251, x=0, y=0)

        block1 = Entry(topVector2d, font="Tahoma", justify="center")
        block1.place(height=69, width=69, x=385, y=218)
        block2 = Entry(topVector2d, font="Tahoma", justify="center")
        block2.place(height=69, width=69, x=472, y=218)
        block3 = Entry(topVector2d, font="Tahoma", justify="center")
        block3.place(height=69, width=69, x=385, y=317)
        block4 = Entry(topVector2d, font="Tahoma", justify="center")
        block4.place(height=69, width=69, x=472, y=317)

        addButton = Button(topVector2d, font="Tahoma 15 bold", text="Addition", background="lightblue",
                           command=lambda: Addition(float(block1.get()), float(block2.get()),
                                                    float(block3.get()), float(block4.get())))
        addButton.place(height=59, width=230, x=665, y=83)
        subButton = Button(topVector2d, font="Tahoma 15 bold", text="Subtraction", background="lightblue",
                           command=lambda: Subtraction(float(block1.get()), float(block2.get()),
                                                       float(block3.get()), float(block4.get())))
        subButton.place(height=59, width=230, x=915, y=83)
        dotButton = Button(topVector2d, font="Tahoma 15 bold", text="Dot Product", background="lightblue",
                           command=lambda: DotProduct(float(block1.get()), float(block2.get()),
                                                      float(block3.get()), float(block4.get())))
        dotButton.place(height=59, width=230, x=665, y=167)
        magButton = Button(topVector2d, font="Tahoma 15 bold", text="Magnitude", background="lightblue",
                           command=lambda: Magnitude(float(block1.get()), float(block2.get())))
        magButton.place(height=59, width=230, x=915, y=167)
        angleButton = Button(topVector2d, font="Tahoma 15 bold", text="Finding Angle", background="lightblue",
                             command=lambda: FindingAngle(float(block1.get()), float(block2.get()),
                                                          float(block3.get()), float(block4.get())))
        angleButton.place(height=59, width=230, x=665, y=254)
        unitButton = Button(topVector2d, font="Tahoma 15 bold", text="Unit Vector", background="lightblue",
                            command=lambda: UnitVector(float(block1.get()), float(block2.get())))
        unitButton.place(height=59, width=230, x=915, y=254)
        orthogonalityButton = Button(topVector2d, font="Tahoma 15 bold", text="Orthogonality", background="lightblue",
                                     command=lambda: Orthogonality(float(block1.get()), float(block2.get()),
                                                                   float(block3.get()), float(block4.get())))
        orthogonalityButton.place(height=59, width=230, x=665, y=336)
        parallelButton = Button(topVector2d, font="Tahoma 15 bold", text="Parallelism", background="lightblue",
                                command=lambda: Parallelism(float(block1.get()), float(block2.get()),
                                                            float(block3.get()), float(block4.get())))
        parallelButton.place(height=59, width=230, x=915, y=336)

        def open_info2dvector():
            topinfo2dvector = Toplevel()
            topinfo2dvector.title("2D Vector Calculator")
            topinfo2dvector.geometry("1251x703+120+50")
            topVector2d.withdraw()

            winsound.PlaySound("avangersinfo.wav", winsound.SND_ASYNC)

            info2dvector = PhotoImage(file="info2dvector.png")
            label = Label(topinfo2dvector, image=info2dvector)
            label.image = info2dvector
            label.place(height=703, width=1251, x=0, y=0)

            closeButton = PhotoImage(file="closeButton.png")
            label = Button(topinfo2dvector, image=closeButton, command=lambda: (topVector2d.deiconify(), topinfo2dvector.destroy()))
            label.image = closeButton
            label.place(height=66, width=70, x=1172, y=410)

        infoButton = PhotoImage(file="infoButton.png")
        label = Button(topVector2d, image=infoButton, command=open_info2dvector)
        label.image = infoButton
        label.place(height=66, width=70, x=1172, y=410)
        ResetButton = PhotoImage(file="ResetButton.png")
        label = Button(topVector2d, image=ResetButton, command=delete)
        label.image = ResetButton
        label.place(height=66, width=70, x=1172, y=483)
        BackButton = PhotoImage(file="BackButton.png")
        label = Button(topVector2d, image=BackButton, command=lambda: (topVectorMenu.deiconify(), topVector2d.destroy()))
        label.image = BackButton
        label.place(height=66, width=70, x=1172, y=556)
        ExitButton = PhotoImage(file="ExitButton.png")
        label = Button(topVector2d, image=ExitButton, command=lambda: closeprogram())
        label.image = ExitButton
        label.place(height=66, width=70, x=1172, y=629)

        OutputPlace = Label(topVector2d, text=" ", background="#030706")
        OutputPlace.place(height=50, width=370, x=438, y=530)

    def openVector3d():
        def Addition(i1, j1, k1, i2, j2, k2):
            ans = (round(i1 + i2, 2), round(j1 + j2, 2), round(k1 + k2, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def Subtraction(i1, j1, k1, i2, j2, k2):
            ans = (round(i1 - i2, 2), round(j1 - j2, 2), round(k1 - k2, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def DotProduct(i1, j1, k1, i2, j2, k2):
            ans = (round(i1 * i2, 2), round(j1 * j2, 2), round(k1 * k2, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def CrossProduct(i1, j1, k1, i2, j2, k2):
            a = j1 * k2 - k1 * j2
            b = k1 * i2 - i1 * k2
            c = i1 * j2 - j1 * i2
            ans = (round(a, 2), round(b, 2), round(c, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def Magnitude(i1, j1, k1):
            ans = (round(((i1 ** 2 + j1 ** 2 + k1 ** 2) ** (1 / 2)), 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text="Magnitude (Vector A) = " + str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def FindingAngle(i1, j1, k1, i2, j2, k2):
            a = i1 * i2 + j1 * j2 + k1 * k2
            b = (i1 ** 2 + j1 ** 2 + k1 ** 2) ** (1 / 2)
            c = (i2 ** 2 + j2 ** 2 + k2 ** 2) ** (1 / 2)
            d = a / (b * c)
            ans = round(math.degrees(math.acos(d)), 2)
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text="Angle (in degree) = " + str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def UnitVector(i1, j1, k1):
            a = (i1 ** 2 + j1 ** 2 + k1 ** 2) ** (1 / 2)
            ans = (round(i1 / a, 2), round(j1 / a, 2), round(k1 / a, 2))
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold",
                                text="Unit Vector (Vector A)" + "\n""= " + str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def Orthogonality(i1, j1, k1, i2, j2, k2):
            a = i1 * i2 + j1 * j2 + k1 * k2
            if a == 0:
                ans = ("Perpendicular")
            elif a != 0:
                ans = ("Not perpendicular")
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def Parallelism(i1, j1, k1, i2, j2, k2):
            a = i1 / i2
            b = j1 / j2
            c = k1 / k2
            if a == b == c:
                ans = ("Parallel")
            else:
                ans = ("Not Parallel")
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=str(ans),
                                foreground="#70f5de", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        def delete():
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block4.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            winsound.PlaySound("soundEffect1.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            OutputPlace = Label(topVector3d, font="Tahoma 15 bold", text=" ", background="#030706")
            OutputPlace.place(height=50, width=370, x=369, y=535)

        topVector3d = Toplevel()
        topVector3d.title("3D Vector Calculator")
        topVector3d.geometry("1251x703+120+50")
        topVectorMenu.withdraw()

        winsound.PlaySound("sound1_3.wav", winsound.SND_ASYNC)

        vector3D = PhotoImage(file="vector3D.png")
        label = Label(topVector3d, image=vector3D)
        label.image = vector3D
        label.place(height=703, width=1251, x=0, y=0)

        block1 = Entry(topVector3d, font="Tahoma", justify="center")
        block1.place(height=79, width=79, x=428, y=238)
        block2 = Entry(topVector3d, font="Tahoma", justify="center")
        block2.place(height=79, width=79, x=527, y=238)
        block3 = Entry(topVector3d, font="Tahoma", justify="center")
        block3.place(height=79, width=79, x=626, y=238)
        block4 = Entry(topVector3d, font="Tahoma", justify="center")
        block4.place(height=79, width=79, x=428, y=351)
        block5 = Entry(topVector3d, font="Tahoma", justify="center")
        block5.place(height=79, width=79, x=527, y=351)
        block6 = Entry(topVector3d, font="Tahoma", justify="center")
        block6.place(height=79, width=79, x=626, y=351)

        addButton = Button(topVector3d, font="Tahoma 15 bold", text="Addition", background="lightblue",
                           command=lambda: Addition(float(block1.get()), float(block2.get()), float(block3.get()),
                                                    float(block4.get()), float(block5.get()), float(block6.get())))
        addButton.place(height=59, width=230, x=741, y=94)
        subButton = Button(topVector3d, font="Tahoma 15 bold", text="Subtraction", background="lightblue",
                           command=lambda: Subtraction(float(block1.get()), float(block2.get()),
                                                       float(block3.get()), float(block4.get()),
                                                       float(block5.get()), float(block6.get())))
        subButton.place(height=59, width=230, x=989, y=94)
        dotButton = Button(topVector3d, font="Tahoma 15 bold", text="Dot Product", background="lightblue",
                           command=lambda: DotProduct(float(block1.get()), float(block2.get()), float(block3.get()),
                                                      float(block4.get()), float(block5.get()), float(block6.get())))
        dotButton.place(height=59, width=230, x=741, y=160)
        crossButton = Button(topVector3d, font="Tahoma 15 bold", text="Cross Product", background="lightblue",
                             command=lambda: CrossProduct(float(block1.get()), float(block2.get()), float(block3.get()),
                                                          float(block4.get()), float(block5.get()), float(block6.get())))
        crossButton.place(height=59, width=230, x=989, y=160)
        magButton = Button(topVector3d, font="Tahoma 15 bold", text="Magnitude", background="lightblue",
                           command=lambda: Magnitude(float(block1.get()), float(block2.get()), float(block3.get())))
        magButton.place(height=59, width=230, x=741, y=226)
        angleButton = Button(topVector3d, font="Tahoma 15 bold", text="Finding Angle", background="lightblue",
                             command=lambda: FindingAngle(float(block1.get()), float(block2.get()), float(block3.get()),
                                                          float(block4.get()), float(block5.get()), float(block6.get())))
        angleButton.place(height=59, width=230, x=989, y=226)
        unitButton = Button(topVector3d, font="Tahoma 15 bold", text="Unit Vector", background="lightblue",
                            command=lambda: UnitVector(float(block1.get()), float(block2.get()), float(block3.get())))
        unitButton.place(height=59, width=230, x=741, y=292)
        orthogonalityButton = Button(topVector3d, font="Tahoma 15 bold", text="Orthogonality", background="lightblue",
                                     command=lambda: Orthogonality(float(block1.get()), float(block2.get()), float(block3.get()),
                                                                   float(block4.get()), float(block5.get()), float(block6.get())))
        orthogonalityButton.place(height=59, width=230, x=989, y=292)
        parallelButton = Button(topVector3d, font="Tahoma 15 bold", text="Parallelism", background="lightblue",
                                command=lambda: Parallelism(float(block1.get()), float(block2.get()), float(block3.get()),
                                                            float(block4.get()), float(block5.get()), float(block6.get())))
        parallelButton.place(height=59, width=230, x=741, y=358)

        def open_info3dvector():
            topinfo3dvector = Toplevel()
            topinfo3dvector.title("3D Vector Calculator")
            topinfo3dvector.geometry("1251x703+120+50")
            topVector3d.withdraw()

            winsound.PlaySound("avangersinfo.wav", winsound.SND_ASYNC)

            info3dvector = PhotoImage(file="info3dvector.png")
            label = Label(topinfo3dvector, image=info3dvector)
            label.image = info3dvector
            label.place(height=703, width=1251, x=0, y=0)

            closeButton = PhotoImage(file="closeButton.png")
            label = Button(topinfo3dvector, image=closeButton, command=lambda: (topVector3d.deiconify(), topinfo3dvector.destroy()))
            label.image = closeButton
            label.place(height=66, width=70, x=1172, y=410)

        infoButton = PhotoImage(file="infoButton.png")
        label = Button(topVector3d, image=infoButton, command=open_info3dvector)
        label.image = infoButton
        label.place(height=66, width=70, x=1172, y=410)
        ResetButton = PhotoImage(file="ResetButton.png")
        label = Button(topVector3d, image=ResetButton, command=delete)
        label.image = ResetButton
        label.place(height=66, width=70, x=1172, y=483)
        BackButton = PhotoImage(file="BackButton.png")
        label = Button(topVector3d, image=BackButton,
                       command=lambda: (topVectorMenu.deiconify(), topVector3d.destroy()))
        label.image = BackButton
        label.place(height=66, width=70, x=1172, y=556)
        ExitButton = PhotoImage(file="ExitButton.png")
        label = Button(topVector3d, image=ExitButton, command=lambda: closeprogram())
        label.image = ExitButton
        label.place(height=66, width=70, x=1172, y=629)

        OutputPlace = Label(topVector3d, text=" ", background="#030706")
        OutputPlace.place(height=50, width=370, x=369, y=535)

    buttonVector2d = PhotoImage(file="buttonVector2d.png")
    label = Button(topVectorMenu, image=buttonVector2d, command=openVector2d)
    label.image = buttonVector2d
    label.place(height=59, width=240, x=505, y=461)
    buttonVector3d = PhotoImage(file="buttonVector3d.png")
    label = Button(topVectorMenu, image=buttonVector3d, command=openVector3d)
    label.image = buttonVector3d
    label.place(height=59, width=240, x=505, y=570)

    BackButton = PhotoImage(file="BackButton.png")
    label = Button(topVectorMenu, image=BackButton, command=lambda: (root.deiconify(), topVectorMenu.destroy()))
    label.image = BackButton
    label.place(height=66, width=70, x=1172, y=556)
    ExitButton = PhotoImage(file="ExitButton.png")
    label = Button(topVectorMenu, image=ExitButton, command=lambda: closeprogram())
    label.image = ExitButton
    label.place(height=66, width=70, x=1172, y=629)

def openmatrixMenu():
    topMatrixMenu = Toplevel()
    topMatrixMenu.title("Matrix Calculator")
    topMatrixMenu.geometry("1251x703+120+50")
    root.withdraw()

    winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)

    matrixMenu = PhotoImage(file="matrixMenu.png")
    label = Label(topMatrixMenu, image=matrixMenu)
    label.image = matrixMenu
    label.place(height=703, width=1251, x=0, y=0)

    def open2dMatrix():
        top2dMatrix = Toplevel()
        top2dMatrix.title("2D Matrix Calculator")
        top2dMatrix.geometry("1251x703+120+50")
        topMatrixMenu.withdraw()

        winsound.PlaySound("hawaii.wav", winsound.SND_ASYNC)

        matrixTWOd = PhotoImage(file="matrixTWOd.png")
        label = Label(top2dMatrix, image=matrixTWOd)
        label.image = matrixTWOd
        label.place(height=703, width=1251, x=0, y=0)

        def Addition(a, b, c, d, e, f, g, h):
            ans1 = round(a + e, 2)
            ans2 = round(b + f, 2)
            ans3 = round(c + g, 2)
            ans4 = round(d + h, 2)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\n" + "\n" + str(ans3) + "\t" + str(ans4),
                                foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        def Subtraction(a, b, c, d, e, f, g, h):
            ans1 = round(a - e, 2)
            ans2 = round(b - f, 2)
            ans3 = round(c - g, 2)
            ans4 = round(d - h, 2)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\n" + "\n" + str(ans3) + "\t" + str(ans4),
                                foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        def Multiplication(a, b, c, d, e, f, g, h):
            ans1 = round(a * e + b * g, 2)
            ans2 = round(a * f + b * h, 2)
            ans3 = round(c * e + d * g, 2)
            ans4 = round(c * f + d * h, 2)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\n" + "\n" + str(ans3) + "\t" + str(ans4),
                                foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        def MultiplyBy(a, b, c, d, k):
            ans1 = round(a * k, 2)
            ans2 = round(b * k, 2)
            ans3 = round(c * k, 2)
            ans4 = round(d * k, 2)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\n" + "\n" + str(ans3) + "\t" + str(ans4),
                                foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        def Transpose(a, b, c, d):
            ans1 = round(a, 2)
            ans2 = round(c, 2)
            ans3 = round(b, 2)
            ans4 = round(d, 2)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                text="Transpose"+"\n"+"\n"+str(ans1) + "\t" + str(ans2) + "\n" + "\n" + str(ans3) + "\t" + str(ans4),
                                foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        def Determinant(a, b, c, d):
            ans = round(a * d - c * b, 2)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold", text="Determinant"+"\n"+"\n"+str(ans),
                                foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        def Inverse(a, b, c, d):
            k = a * d - c * b
            if k == 0:
                winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                    text="Inverse" + "\n" + "\n" + "No Inverse",
                                    foreground="white", background="#030706")
                OutputPlace.place(height=148, width=285, x=496, y=218)
            else:
                ans1 = round((1 / k) * d, 2)
                ans2 = round((1 / k) * -b, 2)
                ans3 = round((1 / k) * -c, 2)
                ans4 = round((1 / k) * a, 2)
                winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold",
                                    text="Inverse"+"\n"+"\n"+str(ans1) + "\t" + str(ans2) + "\n" + "\n" + str(ans3) + "\t" + str(ans4),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=148, width=285, x=496, y=218)

        def delete():
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block4.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            block7.delete(first=0, last=100)
            block8.delete(first=0, last=100)
            block9.delete(first=0, last=100)
            block11.delete(first=0, last=100)
            winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
            OutputPlace.place(height=148, width=285, x=496, y=218)

        block1 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block1.place(height=41, width=73, x=188, y=57)
        block2 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block2.place(height=41, width=73, x=290, y=57)
        block3 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block3.place(height=41, width=73, x=188, y=112)
        block4 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block4.place(height=41, width=73, x=290, y=112)
        block5 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block5.place(height=41, width=73, x=911, y=57)
        block6 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block6.place(height=41, width=73, x=1011, y=57)
        block7 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block7.place(height=41, width=73, x=911, y=112)
        block8 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block8.place(height=41, width=73, x=1011, y=112)
        block9 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block9.place(height=37, width=73, x=325, y=368)
        block11 = Entry(top2dMatrix, font="Tahoma", justify="center")
        block11.place(height=37, width=73, x=1045, y=370)

        addButton = Button(top2dMatrix, font="Tahoma 15 bold", text="+", background="brown",
                           command=lambda: Addition(float(block1.get()), float(block2.get()),
                                                    float(block3.get()), float(block4.get()),
                                                    float(block5.get()), float(block6.get()),
                                                    float(block7.get()), float(block8.get())))
        addButton.place(height=51, width=55, x=513, y=98)
        minusButton = Button(top2dMatrix, font="Tahoma 15 bold", text="-", background="brown",
                             command=lambda: Subtraction(float(block1.get()), float(block2.get()),
                                                         float(block3.get()), float(block4.get()),
                                                         float(block5.get()), float(block6.get()),
                                                         float(block7.get()), float(block8.get())))
        minusButton.place(height=51, width=55, x=607, y=98)
        mulButton = Button(top2dMatrix, font="Tahoma 15 bold", text="x", background="brown",
                           command=lambda: Multiplication(float(block1.get()), float(block2.get()),
                                                          float(block3.get()), float(block4.get()),
                                                          float(block5.get()), float(block6.get()),
                                                          float(block7.get()), float(block8.get())))
        mulButton.place(height=51, width=55, x=699, y=98)

        inverButton1 = PhotoImage(file="inverseButton.png")
        label = Button(top2dMatrix, image=inverButton1,
                       command=lambda: Inverse(float(block1.get()), float(block2.get()),
                                               float(block3.get()), float(block4.get())))
        label.image = inverButton1
        label.place(height=37, width=244, x=154, y=192)
        determinantButton1 = PhotoImage(file="determinantButton.png")
        label = Button(top2dMatrix, image=determinantButton1,
                       command=lambda: Determinant(float(block1.get()), float(block2.get()),
                                                   float(block3.get()), float(block4.get())))
        label.image = determinantButton1
        label.place(height=37, width=244, x=154, y=253)
        transposeButton1 = PhotoImage(file="transposeButton.png")
        label = Button(top2dMatrix, image=transposeButton1,
                       command=lambda: Transpose(float(block1.get()), float(block2.get()),
                                                 float(block3.get()), float(block4.get())))
        label.image = transposeButton1
        label.place(height=37, width=244, x=154, y=314)
        multiplyByButton1 = PhotoImage(file="multiplyByButton.png")
        label = Button(top2dMatrix, image=multiplyByButton1,
                       command=lambda: MultiplyBy(float(block1.get()), float(block2.get()),
                                                  float(block3.get()), float(block4.get()),
                                                  float(block9.get())))
        label.image = multiplyByButton1
        label.place(height=37, width=171, x=154, y=368)
        inverButton2 = PhotoImage(file="inverseButton.png")
        label = Button(top2dMatrix, image=inverButton2,
                       command=lambda: Inverse(float(block5.get()), float(block6.get()),
                                               float(block7.get()), float(block8.get())))
        label.image = inverButton2
        label.place(height=37, width=244, x=874, y=194)
        determinantButton2 = PhotoImage(file="determinantButton.png")
        label = Button(top2dMatrix, image=determinantButton2,
                       command=lambda: Determinant(float(block5.get()), float(block6.get()),
                                                   float(block7.get()), float(block8.get())))
        label.image = determinantButton2
        label.place(height=37, width=244, x=874, y=255)
        transposeButton2 = PhotoImage(file="transposeButton.png")
        label = Button(top2dMatrix, image=transposeButton2,
                       command=lambda: Transpose(float(block5.get()), float(block6.get()),
                                                 float(block7.get()), float(block8.get())))
        label.image = transposeButton2
        label.place(height=37, width=244, x=874, y=316)
        multiplyByButton2 = PhotoImage(file="multiplyByButton.png")
        label = Button(top2dMatrix, image=multiplyByButton2,
                       command=lambda: MultiplyBy(float(block5.get()), float(block6.get()),
                                                  float(block7.get()), float(block8.get()),
                                                  float(block11.get())))
        label.image = multiplyByButton2
        label.place(height=37, width=171, x=874, y=370)

        def open_info2dmatrix():
            topinfo2dmatrix = Toplevel()
            topinfo2dmatrix.title("2D Matrix Calculator")
            topinfo2dmatrix.geometry("1251x703+120+50")
            top2dMatrix.withdraw()

            winsound.PlaySound("hawaiiinfo.wav", winsound.SND_ASYNC)

            info2dmatrix = PhotoImage(file="info2dmatrix.png")
            label = Label(topinfo2dmatrix, image=info2dmatrix)
            label.image = info2dmatrix
            label.place(height=703, width=1251, x=0, y=0)

            closeButton = PhotoImage(file="closeButton.png")
            label = Button(topinfo2dmatrix, image=closeButton, command=lambda: (top2dMatrix.deiconify(), topinfo2dmatrix.destroy()))
            label.image = closeButton
            label.place(height=66, width=70, x=1172, y=410)

        infoButton = PhotoImage(file="infoButton.png")
        label = Button(top2dMatrix, image=infoButton, command=open_info2dmatrix)
        label.image = infoButton
        label.place(height=66, width=70, x=1172, y=410)
        ResetButton = PhotoImage(file="ResetButton.png")
        label = Button(top2dMatrix, image=ResetButton, command=delete)
        label.image = ResetButton
        label.place(height=66, width=70, x=1172, y=483)
        BackButton = PhotoImage(file="BackButton.png")
        label = Button(top2dMatrix, image=BackButton,
                       command=lambda: (topMatrixMenu.deiconify(), top2dMatrix.destroy()))
        label.image = BackButton
        label.place(height=66, width=70, x=1172, y=556)
        ExitButton = PhotoImage(file="ExitButton.png")
        label = Button(top2dMatrix, image=ExitButton, command=lambda: closeprogram())
        label.image = ExitButton
        label.place(height=66, width=70, x=1172, y=629)

        OutputPlace = Label(top2dMatrix, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
        OutputPlace.place(height=148, width=285, x=496, y=218)

    def open2dTrans():
        top2dTrans = Toplevel()
        top2dTrans.title("2D Transformation Calculator")
        top2dTrans.geometry("1251x703+120+50")
        topMatrixMenu.withdraw()

        winsound.PlaySound("yoohoo.wav", winsound.SND_ASYNC)

        def ReflectX(a, b):
            ans1 = round(1 * a + 0 * b, 2)
            ans2 = round(0 * a + -1 * b, 2)
            winsound.PlaySound("hahaha1.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Reflection (x-axis)"+ "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def ReflectY(a, b):
            ans1 = round(-1 * a + 0 * b, 2)
            ans2 = round(0 * a + 1 * b, 2)
            winsound.PlaySound("hahaha2.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Reflection (y-axis)"+ "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def ReflectO(a, b):
            ans1 = round(-1 * a + 0 * b, 2)
            ans2 = round(0 * a + -1 * b, 2)
            winsound.PlaySound("hahaha3.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Reflection (origin)"+ "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def ReflectYX(a, b):
            ans1 = round(0 * a + 1 * b, 2)
            ans2 = round(1 * a + 0 * b, 2)
            winsound.PlaySound("hahaha4.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Reflection (y = x)" + "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def Rotation(a, b, d):
            d1 = math.radians(d)
            e = math.cos(d1)
            f = math.sin(d1)
            g = math.sin(d1)
            h = math.cos(d1)
            ans1 = round(e * a + f * b, 2)
            ans2 = round(-g * a + h * b, 2)
            winsound.PlaySound("hahaha5.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Rotation" + "\n" + "\n" + str(ans1) + "\n"
                                                                        + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def Translation(a, b, x, y):
            ans1 = round(a + x, 2)
            ans2 = round(b + y, 2)
            winsound.PlaySound("hahaha6.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Translation"+ "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def ShearX(a, b, x):
            ans1 = round(1 * a + x * b, 2)
            ans2 = round(0 * a + 1 * b, 2)
            winsound.PlaySound("hahaha7.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Shear Horizontally" + "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def ShearY(a, b, y):
            ans1 = round(1 * a + 0 * b, 2)
            ans2 = round(y * a + 1 * b, 2)
            winsound.PlaySound("hahaha8.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Shear Vertically"+ "\n" + "\n"
                                                                        + str(ans1) + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        def Scale(a, b, x, y):
            ans1 = round(x * a + 0 * b, 2)
            ans2 = round(0 * a + y * b, 2)
            winsound.PlaySound("hahaha9.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text="Scaling"+ "\n" + "\n" + str(ans1)
                                                                        + "\n" + "\n" + str(ans2),
                                foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        matrixTrans = PhotoImage(file="matrixTrans.png")
        label = Label(top2dTrans, image=matrixTrans)
        label.image = matrixTrans
        label.place(height=703, width=1251, x=0, y=0)

        block1 = Entry(top2dTrans, font="Tahoma", justify="center")
        block1.place(height=41, width=73, x=193, y=96)
        block2 = Entry(top2dTrans, font="Tahoma", justify="center")
        block2.place(height=41, width=73, x=193, y=152)
        blockdegree = Entry(top2dTrans, font="Tahoma", justify="center")
        blockdegree.place(height=47, width=73, x=932, y=24)
        blocktrans_x = Entry(top2dTrans, font="Tahoma", justify="center")
        blocktrans_x.place(height=37, width=73, x=859, y=84)
        blocktrans_y = Entry(top2dTrans, font="Tahoma", justify="center")
        blocktrans_y.place(height=37, width=73, x=932, y=84)
        blockshear_h = Entry(top2dTrans, font="Tahoma", justify="center")
        blockshear_h.place(height=37, width=73, x=859, y=144)
        blockshear_v = Entry(top2dTrans, font="Tahoma", justify="center")
        blockshear_v.place(height=37, width=73, x=859, y=204)
        blockscale_x = Entry(top2dTrans, font="Tahoma", justify="center")
        blockscale_x.place(height=37, width=73, x=859, y=264)
        blockscale_y = Entry(top2dTrans, font="Tahoma", justify="center")
        blockscale_y.place(height=37, width=73, x=932, y=264)

        def delete():
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            blockdegree.delete(first=0, last=100)
            blocktrans_x.delete(first=0, last=100)
            blocktrans_y.delete(first=0, last=100)
            blockshear_h.delete(first=0, last=100)
            blockshear_v.delete(first=0, last=100)
            blockscale_x.delete(first=0, last=100)
            blockscale_y.delete(first=0, last=100)
            winsound.PlaySound("hahaha10.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
            OutputPlace.place(height=165, width=307, x=472, y=360)

        refxButton = PhotoImage(file="refxButton.png")
        label = Button(top2dTrans, image=refxButton, command=lambda: ReflectX(float(block1.get()), float(block2.get())))
        label.image = refxButton
        label.place(height=37, width=244, x=408, y=24)
        refyButton = PhotoImage(file="refyButton.png")
        label = Button(top2dTrans, image=refyButton, command=lambda: ReflectY(float(block1.get()), float(block2.get())))
        label.image = refyButton
        label.place(height=37, width=244, x=408, y=84)
        refoButton = PhotoImage(file="refoButton.png")
        label = Button(top2dTrans, image=refoButton, command=lambda: ReflectO(float(block1.get()), float(block2.get())))
        label.image = refoButton
        label.place(height=37, width=244, x=408, y=144)
        refyxButton = PhotoImage(file="refyxButton.png")
        label = Button(top2dTrans, image=refyxButton,
                       command=lambda: ReflectYX(float(block1.get()), float(block2.get())))
        label.image = refyxButton
        label.place(height=37, width=244, x=408, y=204)
        rotationButton = PhotoImage(file="rotationButton.png")
        label = Button(top2dTrans, image=rotationButton,
                       command=lambda: Rotation(float(block1.get()), float(block2.get()),
                                                float(blockdegree.get())))
        label.image = rotationButton
        label.place(height=47, width=244, x=688, y=24)
        translationButton = PhotoImage(file="translationButton.png")
        label = Button(top2dTrans, image=translationButton,
                       command=lambda: Translation(float(block1.get()), float(block2.get()),
                                                   float(blocktrans_x.get()), float(blocktrans_y.get())))
        label.image = translationButton
        label.place(height=37, width=171, x=688, y=84)
        shearHButton = PhotoImage(file="shearHButton.png")
        label = Button(top2dTrans, image=shearHButton,
                       command=lambda: ShearX(float(block1.get()), float(block2.get()), float(blockshear_h.get())))
        label.image = shearHButton
        label.place(height=37, width=171, x=688, y=144)
        shearVButton = PhotoImage(file="shearVButton.png")
        label = Button(top2dTrans, image=shearVButton,
                       command=lambda: ShearY(float(block1.get()), float(block2.get()), float(blockshear_v.get())))
        label.image = shearVButton
        label.place(height=37, width=171, x=688, y=204)
        scalingButton = PhotoImage(file="scalingButton.png")
        label = Button(top2dTrans, image=scalingButton,
                       command=lambda: Scale(float(block1.get()), float(block2.get()),
                                             float(blockscale_x.get()), float(blockscale_y.get())))
        label.image = scalingButton
        label.place(height=37, width=171, x=688, y=264)

        def open_info2dtransformation():
            topinfo2dtransformation = Toplevel()
            topinfo2dtransformation.title("2D Transformation Calculator")
            topinfo2dtransformation.geometry("1251x703+120+50")
            top2dTrans.withdraw()

            winsound.PlaySound("hahaha10.wav", winsound.SND_ASYNC)

            info2dtransformation = PhotoImage(file="info2dtransformation.png")
            label = Label(topinfo2dtransformation, image=info2dtransformation)
            label.image = info2dtransformation
            label.place(height=703, width=1251, x=0, y=0)

            closeButton = PhotoImage(file="closeButton.png")
            label = Button(topinfo2dtransformation, image=closeButton, command=lambda: (top2dTrans.deiconify(), topinfo2dtransformation.destroy()))
            label.image = closeButton
            label.place(height=66, width=70, x=1172, y=410)

        infoButton = PhotoImage(file="infoButton.png")
        label = Button(top2dTrans, image=infoButton, command=open_info2dtransformation)
        label.image = infoButton
        label.place(height=66, width=70, x=1172, y=410)
        ResetButton = PhotoImage(file="ResetButton.png")
        label = Button(top2dTrans, image=ResetButton, command=delete)
        label.image = ResetButton
        label.place(height=66, width=70, x=1172, y=483)
        BackButton = PhotoImage(file="BackButton.png")
        label = Button(top2dTrans, image=BackButton,
                       command=lambda: (topMatrixMenu.deiconify(), top2dTrans.destroy()))
        label.image = BackButton
        label.place(height=66, width=70, x=1172, y=556)
        ExitButton = PhotoImage(file="ExitButton.png")
        label = Button(top2dTrans, image=ExitButton, command=lambda: closeprogram())
        label.image = ExitButton
        label.place(height=66, width=70, x=1172, y=629)

        OutputPlace = Label(top2dTrans, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
        OutputPlace.place(height=165, width=307, x=472, y=360)

    def open3dMatrix():
        top3dMatrix = Toplevel()
        top3dMatrix.title("3D Matrix Calculator")
        top3dMatrix.geometry("1251x703+120+50")
        topMatrixMenu.withdraw()

        winsound.PlaySound("fight.wav", winsound.SND_ASYNC)

        matrixTHREEd = PhotoImage(file="matrixTHREEd.png")
        label = Label(top3dMatrix, image=matrixTHREEd)
        label.image = matrixTHREEd
        label.place(height=703, width=1251, x=0, y=0)

        def Addition(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r):
            ans1 = round(a + j, 2)
            ans2 = round(b + k, 2)
            ans3 = round(c + l, 2)
            ans4 = round(d + m, 2)
            ans5 = round(e + n, 2)
            ans6 = round(f + o, 2)
            ans7 = round(g + p, 2)
            ans8 = round(h + q, 2)
            ans9 = round(i + r, 2)
            winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) +
                                     "\n" + "\n" + str(ans4) + "\t" + str(ans5) + "\t" + str(ans6) +
                                     "\n" + "\n" + str(ans7) + "\t" + str(ans8) + "\t" + str(ans9),
                                foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        def Subtraction(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r):
            ans1 = round(a - j, 2)
            ans2 = round(b - k, 2)
            ans3 = round(c - l, 2)
            ans4 = round(d - m, 2)
            ans5 = round(e - n, 2)
            ans6 = round(f - o, 2)
            ans7 = round(g - p, 2)
            ans8 = round(h - q, 2)
            ans9 = round(i - r, 2)
            winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) +
                                     "\n" + "\n" + str(ans4) + "\t" + str(ans5) + "\t" + str(ans6) +
                                     "\n" + "\n" + str(ans7) + "\t" + str(ans8) + "\t" + str(ans9),
                                foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        def Multiplication(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r):
            ans1 = round(a * j + b * m + c * p, 2)
            ans2 = round(a * k + b * n + c * q, 2)
            ans3 = round(a * l + b * o + c * r, 2)
            ans4 = round(d * j + e * m + f * p, 2)
            ans5 = round(d * k + e * n + f * q, 2)
            ans6 = round(d * l + e * o + f * r, 2)
            ans7 = round(g * j + h * m + i * p, 2)
            ans8 = round(g * k + h * n + i * q, 2)
            ans9 = round(g * l + h * o + i * r, 2)
            winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) +
                                     "\n" + "\n" + str(ans4) + "\t" + str(ans5) + "\t" + str(ans6) +
                                     "\n" + "\n" + str(ans7) + "\t" + str(ans8) + "\t" + str(ans9),
                                foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        def MultiplyBy(a, b, c, d, e, f, g, h, i, k):
            ans1 = round(a * k, 2)
            ans2 = round(b * k, 2)
            ans3 = round(c * k, 2)
            ans4 = round(d * k, 2)
            ans5 = round(e * k, 2)
            ans6 = round(f * k, 2)
            ans7 = round(g * k, 2)
            ans8 = round(h * k, 2)
            ans9 = round(i * k, 2)
            winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) +
                                     "\n" + "\n" + str(ans4) + "\t" + str(ans5) + "\t" + str(ans6) +
                                     "\n" + "\n" + str(ans7) + "\t" + str(ans8) + "\t" + str(ans9),
                                foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        def Transpose(a, b, c, d, e, f, g, h, i):
            ans1 = round(a, 2)
            ans2 = round(d, 2)
            ans3 = round(g, 2)
            ans4 = round(b, 2)
            ans5 = round(e, 2)
            ans6 = round(h, 2)
            ans7 = round(c, 2)
            ans8 = round(f, 2)
            ans9 = round(i, 2)
            winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold",
                                text="Transpose"+"\n"+"\n"+str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) +
                                     "\n" + "\n" + str(ans4) + "\t" + str(ans5) + "\t" + str(ans6) +
                                     "\n" + "\n" + str(ans7) + "\t" + str(ans8) + "\t" + str(ans9),
                                foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        def Determinant(a, b, c, d, e, f, g, h, i):
            ans = round(a * (e * i - h * f) - b * (d * i - g * f) + c * (d * h - g * e), 2)
            winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold", text="Determinant"+"\n"+"\n"+str(ans),
                                foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        def Inverse(a, b, c, d, e, f, g, h, i):
            determinant = a * (e * i - h * f) - b * (d * i - g * f) + c * (d * h - g * e)
            ans1 = e * i - f * h
            ans2 = b * i - c * h
            ans3 = b * f - c * e
            ans4 = d * i - f * g
            ans5 = a * i - c * g
            ans6 = a * f - c * d
            ans7 = d * h - e * g
            ans8 = a * h - b * g
            ans9 = a * e - b * d
            newans1 = ans1
            newans2 = -ans2
            newans3 = ans3
            newans4 = -ans4
            newans5 = ans5
            newans6 = -ans6
            newans7 = ans7
            newans8 = -ans8
            newans9 = ans9
            if determinant == 0:
                ans = "No Inverse"
                winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold", text=str(ans),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=160, width=280, x=473, y=243)

            else:
                fans1 = round((1 / determinant) * newans1, 2)
                fans2 = round((1 / determinant) * newans2, 2)
                fans3 = round((1 / determinant) * newans3, 2)
                fans4 = round((1 / determinant) * newans4, 2)
                fans5 = round((1 / determinant) * newans5, 2)
                fans6 = round((1 / determinant) * newans6, 2)
                fans7 = round((1 / determinant) * newans7, 2)
                fans8 = round((1 / determinant) * newans8, 2)
                fans9 = round((1 / determinant) * newans9, 2)
                winsound.PlaySound("punch.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold",
                                    text="Inverse"+"\n"+"\n"+str(fans1) + "\t" + str(fans2) + "\t" + str(fans3) +
                                         "\n" + "\n" + str(fans4) + "\t" + str(fans5) + "\t" + str(fans6) +
                                         "\n" + "\n" + str(fans7) + "\t" + str(fans8) + "\t" + str(fans9),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=160, width=280, x=473, y=243)

        block1 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block1.place(height=41, width=73, x=67, y=77)
        block2 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block2.place(height=41, width=73, x=166, y=77)
        block3 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block3.place(height=41, width=73, x=264, y=77)
        block4 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block4.place(height=41, width=73, x=67, y=132)
        block5 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block5.place(height=41, width=73, x=166, y=132)
        block6 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block6.place(height=41, width=73, x=264, y=132)
        block7 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block7.place(height=41, width=73, x=67, y=187)
        block8 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block8.place(height=41, width=73, x=166, y=187)
        block9 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block9.place(height=37, width=73, x=264, y=187)
        block10 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block10.place(height=37, width=73, x=863, y=77)
        block11 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block11.place(height=37, width=73, x=963, y=77)
        block12 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block12.place(height=37, width=73, x=1065, y=77)
        block13 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block13.place(height=37, width=73, x=863, y=132)
        block14 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block14.place(height=37, width=73, x=963, y=132)
        block15 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block15.place(height=37, width=73, x=1065, y=132)
        block16 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block16.place(height=37, width=73, x=863, y=187)
        block17 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block17.place(height=37, width=73, x=963, y=187)
        block18 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block18.place(height=37, width=73, x=1065, y=187)
        block19 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block19.place(height=37, width=73, x=254, y=441)
        block21 = Entry(top3dMatrix, font="Tahoma", justify="center")
        block21.place(height=37, width=73, x=1048, y=443)

        def delete():
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block4.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            block7.delete(first=0, last=100)
            block8.delete(first=0, last=100)
            block9.delete(first=0, last=100)
            block10.delete(first=0, last=100)
            block11.delete(first=0, last=100)
            block12.delete(first=0, last=100)
            block13.delete(first=0, last=100)
            block14.delete(first=0, last=100)
            block15.delete(first=0, last=100)
            block16.delete(first=0, last=100)
            block17.delete(first=0, last=100)
            block18.delete(first=0, last=100)
            block19.delete(first=0, last=100)
            block21.delete(first=0, last=100)
            winsound.PlaySound("slap.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
            OutputPlace.place(height=160, width=280, x=473, y=243)

        addButton = Button(top3dMatrix, font="Tahoma 15 bold", text="+", background="brown",
                           command=lambda: Addition(float(block1.get()), float(block2.get()), float(block3.get()),
                                                    float(block4.get()), float(block5.get()), float(block6.get()),
                                                    float(block7.get()), float(block8.get()), float(block9.get()),
                                                    float(block10.get()), float(block11.get()), float(block12.get()),
                                                    float(block13.get()), float(block14.get()), float(block15.get()),
                                                    float(block16.get()), float(block17.get()), float(block18.get())))
        addButton.place(height=51, width=55, x=479, y=118)
        minusButton = Button(top3dMatrix, font="Tahoma 15 bold", text="-", background="brown",
                             command=lambda: Subtraction(float(block1.get()), float(block2.get()), float(block3.get()),
                                                         float(block4.get()), float(block5.get()), float(block6.get()),
                                                         float(block7.get()), float(block8.get()), float(block9.get()),
                                                         float(block10.get()), float(block11.get()),
                                                         float(block12.get()),
                                                         float(block13.get()), float(block14.get()),
                                                         float(block15.get()),
                                                         float(block16.get()), float(block17.get()),
                                                         float(block18.get())))
        minusButton.place(height=51, width=55, x=573, y=118)
        mulButton = Button(top3dMatrix, font="Tahoma 15 bold", text="x", background="brown",
                           command=lambda: Multiplication(float(block1.get()), float(block2.get()), float(block3.get()),
                                                          float(block4.get()), float(block5.get()), float(block6.get()),
                                                          float(block7.get()), float(block8.get()), float(block9.get()),
                                                          float(block10.get()), float(block11.get()),
                                                          float(block12.get()),
                                                          float(block13.get()), float(block14.get()),
                                                          float(block15.get()),
                                                          float(block16.get()), float(block17.get()),
                                                          float(block18.get())))
        mulButton.place(height=51, width=55, x=665, y=118)

        inverButton1 = PhotoImage(file="inverseButton.png")
        label = Button(top3dMatrix, image=inverButton1,
                       command=lambda: Inverse(float(block1.get()), float(block2.get()), float(block3.get()),
                                               float(block4.get()), float(block5.get()), float(block6.get()),
                                               float(block7.get()), float(block8.get()), float(block9.get())))
        label.image = inverButton1
        label.place(height=37, width=244, x=83, y=262)
        determinantButton1 = PhotoImage(file="determinantButton.png")
        label = Button(top3dMatrix, image=determinantButton1,
                       command=lambda: Determinant(float(block1.get()), float(block2.get()), float(block3.get()),
                                                   float(block4.get()), float(block5.get()), float(block6.get()),
                                                   float(block7.get()), float(block8.get()), float(block9.get())))
        label.image = determinantButton1
        label.place(height=37, width=244, x=83, y=322)
        transposeButton1 = PhotoImage(file="transposeButton.png")
        label = Button(top3dMatrix, image=transposeButton1,
                       command=lambda: Transpose(float(block1.get()), float(block2.get()), float(block3.get()),
                                                 float(block4.get()), float(block5.get()), float(block6.get()),
                                                 float(block7.get()), float(block8.get()), float(block9.get())))
        label.image = transposeButton1
        label.place(height=37, width=244, x=83, y=382)
        multiplyByButton1 = PhotoImage(file="multiplyByButton.png")
        label = Button(top3dMatrix, image=multiplyByButton1,
                       command=lambda: MultiplyBy(float(block1.get()), float(block2.get()), float(block3.get()),
                                                  float(block4.get()), float(block5.get()), float(block6.get()),
                                                  float(block7.get()), float(block8.get()), float(block9.get()),
                                                  float(block19.get())))
        label.image = multiplyByButton1
        label.place(height=37, width=171, x=83, y=441)
        inverButton2 = PhotoImage(file="inverseButton.png")
        label = Button(top3dMatrix, image=inverButton2,
                       command=lambda: Inverse(float(block10.get()), float(block11.get()), float(block12.get()),
                                               float(block13.get()), float(block14.get()), float(block15.get()),
                                               float(block16.get()), float(block17.get()), float(block18.get())))
        label.image = inverButton2
        label.place(height=37, width=244, x=877, y=260)
        determinantButton2 = PhotoImage(file="determinantButton.png")
        label = Button(top3dMatrix, image=determinantButton2,
                       command=lambda: Determinant(float(block10.get()), float(block11.get()), float(block12.get()),
                                                   float(block13.get()), float(block14.get()), float(block15.get()),
                                                   float(block16.get()), float(block17.get()), float(block18.get())))
        label.image = determinantButton2
        label.place(height=37, width=244, x=877, y=321)
        transposeButton2 = PhotoImage(file="transposeButton.png")
        label = Button(top3dMatrix, image=transposeButton2,
                       command=lambda: Transpose(float(block10.get()), float(block11.get()), float(block12.get()),
                                                 float(block13.get()), float(block14.get()), float(block15.get()),
                                                 float(block16.get()), float(block17.get()), float(block18.get())))
        label.image = transposeButton2
        label.place(height=37, width=244, x=877, y=382)
        multiplyByButton2 = PhotoImage(file="multiplyByButton.png")
        label = Button(top3dMatrix, image=multiplyByButton2,
                       command=lambda: MultiplyBy(float(block10.get()), float(block11.get()), float(block12.get()),
                                                  float(block13.get()), float(block14.get()), float(block15.get()),
                                                  float(block16.get()), float(block17.get()), float(block18.get()),
                                                  float(block21.get())))
        label.image = multiplyByButton2
        label.place(height=37, width=171, x=877, y=443)

        def open_info3dmatrix():
            topinfo3dmatrix = Toplevel()
            topinfo3dmatrix.title("3D Matrix Calculator")
            topinfo3dmatrix.geometry("1251x703+120+50")
            top3dMatrix.withdraw()

            winsound.PlaySound("slap.wav", winsound.SND_ASYNC)

            info3dmatrix = PhotoImage(file="info3dmatrix.png")
            label = Label(topinfo3dmatrix, image=info3dmatrix)
            label.image = info3dmatrix
            label.place(height=703, width=1251, x=0, y=0)

            closeButton = PhotoImage(file="closeButton.png")
            label = Button(topinfo3dmatrix, image=closeButton, command=lambda: (top3dMatrix.deiconify(), topinfo3dmatrix.destroy()))
            label.image = closeButton
            label.place(height=66, width=70, x=1172, y=410)

        infoButton = PhotoImage(file="infoButton.png")
        label = Button(top3dMatrix, image=infoButton, command=open_info3dmatrix)
        label.image = infoButton
        label.place(height=66, width=70, x=1172, y=410)
        ResetButton = PhotoImage(file="ResetButton.png")
        label = Button(top3dMatrix, image=ResetButton, command=delete)
        label.image = ResetButton
        label.place(height=66, width=70, x=1172, y=483)
        BackButton = PhotoImage(file="BackButton.png")
        label = Button(top3dMatrix, image=BackButton,
                       command=lambda: (topMatrixMenu.deiconify(), top3dMatrix.destroy()))
        label.image = BackButton
        label.place(height=66, width=70, x=1172, y=556)
        ExitButton = PhotoImage(file="ExitButton.png")
        label = Button(top3dMatrix, image=ExitButton, command=lambda: closeprogram())
        label.image = ExitButton
        label.place(height=66, width=70, x=1172, y=629)

        OutputPlace = Label(top3dMatrix, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
        OutputPlace.place(height=160, width=280, x=473, y=243)

    def open4dMatrix():
        top4dMatrix = Toplevel()
        top4dMatrix.title("4D Matrix Calculator")
        top4dMatrix.geometry("1251x703+120+50")
        topMatrixMenu.withdraw()

        winsound.PlaySound("crow.wav", winsound.SND_ASYNC)

        def Addition(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, b1, b2, b3, b4, b5, b6, b7,
                     b8, b9, b10, b11, b12, b13, b14, b15, b16):
            ans1 = round(a1 + b1, 2)
            ans2 = round(a2 + b2, 2)
            ans3 = round(a3 + b3, 2)
            ans4 = round(a4 + b4, 2)
            ans5 = round(a5 + b5, 2)
            ans6 = round(a6 + b6, 2)
            ans7 = round(a7 + b7, 2)
            ans8 = round(a8 + b8, 2)
            ans9 = round(a9 + b9, 2)
            ans10 = round(a10 + b10, 2)
            ans11 = round(a11 + b11, 2)
            ans12 = round(a12 + b12, 2)
            ans13 = round(a13 + b13, 2)
            ans14 = round(a14 + b14, 2)
            ans15 = round(a15 + b15, 2)
            ans16 = round(a16 + b16, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def Subtraction(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, b1, b2, b3, b4, b5, b6,
                        b7, b8, b9, b10, b11, b12, b13, b14, b15, b16):
            ans1 = round(a1 - b1, 2)
            ans2 = round(a2 - b2, 2)
            ans3 = round(a3 - b3, 2)
            ans4 = round(a4 - b4, 2)
            ans5 = round(a5 - b5, 2)
            ans6 = round(a6 - b6, 2)
            ans7 = round(a7 - b7, 2)
            ans8 = round(a8 - b8, 2)
            ans9 = round(a9 - b9, 2)
            ans10 = round(a10 - b10, 2)
            ans11 = round(a11 - b11, 2)
            ans12 = round(a12 - b12, 2)
            ans13 = round(a13 - b13, 2)
            ans14 = round(a14 - b14, 2)
            ans15 = round(a15 - b15, 2)
            ans16 = round(a16 - b16, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def Multiplication(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, b1, b2, b3, b4, b5,
                           b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16):
            ans1 = round(a1 * b1 + a2 * b5 + a3 * b9 + a4 * b13, 2)
            ans2 = round(a1 * b2 + a2 * b6 + a3 * b10 + a4 * b14, 2)
            ans3 = round(a1 * b3 + a2 * b7 + a3 * b11 + a4 * b15, 2)
            ans4 = round(a1 * b4 + a2 * b8 + a3 * b12 + a4 * b16, 2)
            ans5 = round(a5 * b1 + a6 * b5 + a7 * b9 + a8 * b13, 2)
            ans6 = round(a5 * b2 + a6 * b6 + a7 * b10 + a8 * b14, 2)
            ans7 = round(a5 * b3 + a6 * b7 + a7 * b11 + a8 * b15, 2)
            ans8 = round(a5 * b4 + a6 * b8 + a7 * b12 + a8 * b16, 2)
            ans9 = round(a9 * b1 + a10 * b5 + a11 * b9 + a12 * b13, 2)
            ans10 = round(a9 * b2 + a10 * b6 + a11 * b10 + a12 * b14, 2)
            ans11 = round(a9 * b3 + a10 * b7 + a11 * b11 + a12 * b15, 2)
            ans12 = round(a9 * b4 + a10 * b8 + a11 * b12 + a12 * b16, 2)
            ans13 = round(a13 * b1 + a14 * b5 + a15 * b9 + a16 * b13, 2)
            ans14 = round(a13 * b2 + a14 * b6 + a15 * b10 + a16 * b14, 2)
            ans15 = round(a13 * b3 + a14 * b7 + a15 * b11 + a16 * b15, 2)
            ans16 = round(a13 * b4 + a14 * b8 + a15 * b12 + a16 * b16, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def MultiplybyFirst(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, k):
            ans1 = round(a1 * k, 2)
            ans2 = round(a2 * k, 2)
            ans3 = round(a3 * k, 2)
            ans4 = round(a4 * k, 2)
            ans5 = round(a5 * k, 2)
            ans6 = round(a6 * k, 2)
            ans7 = round(a7 * k, 2)
            ans8 = round(a8 * k, 2)
            ans9 = round(a9 * k, 2)
            ans10 = round(a10 * k, 2)
            ans11 = round(a11 * k, 2)
            ans12 = round(a12 * k, 2)
            ans13 = round(a13 * k, 2)
            ans14 = round(a14 * k, 2)
            ans15 = round(a15 * k, 2)
            ans16 = round(a16 * k, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def DeterminantFirst(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
            w = a6 * (a11 * a16 - a12 * a15) - a7 * (a10 * a16 - a12 * a14) + a8 * (a10 * a15 - a11 * a14)
            x = a5 * (a11 * a16 - a12 * a15) - a7 * (a9 * a16 - a12 * a13) + a8 * (a9 * a15 - a11 * a13)
            y = a5 * (a10 * a16 - a12 * a14) - a6 * (a9 * a16 - a12 * a13) + a8 * (a9 * a14 - a10 * a13)
            z = a5 * (a10 * a15 - a11 * a14) - a6 * (a9 * a15 - a11 * a13) + a7 * (a9 * a14 - a10 * a13)
            ans = a1 * (w) - a2 * (x) + a3 * (y) - a4 * (z)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold", text="Determinant"+"\n"+"\n"+str(ans),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def TransposeFirst(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
            ans1 = round(a1, 2)
            ans2 = round(a5, 2)
            ans3 = round(a9, 2)
            ans4 = round(a13, 2)
            ans5 = round(a2, 2)
            ans6 = round(a6, 2)
            ans7 = round(a10, 2)
            ans8 = round(a14, 2)
            ans9 = round(a3, 2)
            ans10 = round(a7, 2)
            ans11 = round(a11, 2)
            ans12 = round(a15, 2)
            ans13 = round(a4, 2)
            ans14 = round(a8, 2)
            ans15 = round(a12, 2)
            ans16 = round(a16, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text="Transpose"+"\n"+"\n"+str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def InverseFirst(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
            w = f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n)
            x = e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m)
            y = e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m)
            z = e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m)
            dt = a * (w) - b * (x) + c * (y) - d * (z)

            a1 = -h * k * n + g * l * n + h * j * o - f * l * o - g * j * p + f * k * p
            a2 = d * k * n - c * l * n - d * j * o + b * l * o + c * j * p - b * k * p
            a3 = -d * g * n + c * h * n + d * f * o - b * h * o - c * f * p + b * g * p
            a4 = d * g * j - c * h * j - d * f * k + b * h * k + c * f * l - b * g * l
            a5 = h * k * m - g * l * m - h * i * o + e * l * o + g * i * p - e * k * p
            a6 = -d * k * m + c * l * m + d * i * o - a * l * o - c * i * p + a * k * p
            a7 = d * g * m - c * h * m - d * e * o + a * h * o + c * e * p - a * g * p
            a8 = -d * g * i + c * h * i + d * e * k - a * h * k - c * e * l + a * g * l
            a9 = -h * j * m + f * l * m + h * i * n - e * l * n - f * i * p + e * j * p
            a10 = d * j * m - b * l * m - d * i * n + a * l * n + b * i * p - a * j * p
            a11 = -d * f * m + b * h * m + d * e * n - a * h * n - b * e * p + a * f * p
            a12 = d * f * i - b * h * i - d * e * j + a * h * j + b * e * l - a * f * l
            a13 = g * j * m - f * k * m - g * i * n + e * k * n + f * i * o - e * j * o
            a14 = -c * j * m + b * k * m + c * i * n - a * k * n - b * i * o + a * j * o
            a15 = c * f * m - b * g * m - c * e * n + a * g * n + b * e * o - a * f * o
            a16 = -c * f * i + b * g * i + c * e * j - a * g * j - b * e * k + a * f * k

            if dt == 0:
                ans = "No Inverse"
                winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold", text=str(ans),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=168, width=320, x=470, y=237)

            else:
                ans1 = round(a1 / dt, 2)
                ans2 = round(a2 / dt, 2)
                ans3 = round(a3 / dt, 2)
                ans4 = round(a4 / dt, 2)
                ans5 = round(a5 / dt, 2)
                ans6 = round(a6 / dt, 2)
                ans7 = round(a7 / dt, 2)
                ans8 = round(a8 / dt, 2)
                ans9 = round(a9 / dt, 2)
                ans10 = round(a10 / dt, 2)
                ans11 = round(a11 / dt, 2)
                ans12 = round(a12 / dt, 2)
                ans13 = round(a13 / dt, 2)
                ans14 = round(a14 / dt, 2)
                ans15 = round(a15 / dt, 2)
                ans16 = round(a16 / dt, 2)
                winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                    text="Inverse"+"\n"+"\n"+str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                         "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                         "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                         "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=168, width=320, x=470, y=237)

        def MultiplybySecond(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, k):
            ans1 = round(a1 * k, 2)
            ans2 = round(a2 * k, 2)
            ans3 = round(a3 * k, 2)
            ans4 = round(a4 * k, 2)
            ans5 = round(a5 * k, 2)
            ans6 = round(a6 * k, 2)
            ans7 = round(a7 * k, 2)
            ans8 = round(a8 * k, 2)
            ans9 = round(a9 * k, 2)
            ans10 = round(a10 * k, 2)
            ans11 = round(a11 * k, 2)
            ans12 = round(a12 * k, 2)
            ans13 = round(a13 * k, 2)
            ans14 = round(a14 * k, 2)
            ans15 = round(a15 * k, 2)
            ans16 = round(a16 * k, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text=str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def DeterminantSecond(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
            w = a6 * (a11 * a16 - a12 * a15) - a7 * (a10 * a16 - a12 * a14) + a8 * (a10 * a15 - a11 * a14)
            x = a5 * (a11 * a16 - a12 * a15) - a7 * (a9 * a16 - a12 * a13) + a8 * (a9 * a15 - a11 * a13)
            y = a5 * (a10 * a16 - a12 * a14) - a6 * (a9 * a16 - a12 * a13) + a8 * (a9 * a14 - a10 * a13)
            z = a5 * (a10 * a15 - a11 * a14) - a6 * (a9 * a15 - a11 * a13) + a7 * (a9 * a14 - a10 * a13)
            ans = a1 * (w) - a2 * (x) + a3 * (y) - a4 * (z)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold", text="Determinant"+"\n"+"\n"+str(ans),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def TransposeSecond(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
            ans1 = round(a1, 2)
            ans2 = round(a5, 2)
            ans3 = round(a9, 2)
            ans4 = round(a13, 2)
            ans5 = round(a2, 2)
            ans6 = round(a6, 2)
            ans7 = round(a10, 2)
            ans8 = round(a14, 2)
            ans9 = round(a3, 2)
            ans10 = round(a7, 2)
            ans11 = round(a11, 2)
            ans12 = round(a15, 2)
            ans13 = round(a4, 2)
            ans14 = round(a8, 2)
            ans15 = round(a12, 2)
            ans16 = round(a16, 2)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                text="Transpose"+"\n"+"\n"+
                                     str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                     "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                     "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                     "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                foreground="white", background="#030706")
            OutputPlace.place(height=168, width=320, x=470, y=237)

        def InverseSecond(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
            w = f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n)
            x = e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m)
            y = e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m)
            z = e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m)
            dt = a * (w) - b * (x) + c * (y) - d * (z)

            a1 = -h * k * n + g * l * n + h * j * o - f * l * o - g * j * p + f * k * p
            a2 = d * k * n - c * l * n - d * j * o + b * l * o + c * j * p - b * k * p
            a3 = -d * g * n + c * h * n + d * f * o - b * h * o - c * f * p + b * g * p
            a4 = d * g * j - c * h * j - d * f * k + b * h * k + c * f * l - b * g * l
            a5 = h * k * m - g * l * m - h * i * o + e * l * o + g * i * p - e * k * p
            a6 = -d * k * m + c * l * m + d * i * o - a * l * o - c * i * p + a * k * p
            a7 = d * g * m - c * h * m - d * e * o + a * h * o + c * e * p - a * g * p
            a8 = -d * g * i + c * h * i + d * e * k - a * h * k - c * e * l + a * g * l
            a9 = -h * j * m + f * l * m + h * i * n - e * l * n - f * i * p + e * j * p
            a10 = d * j * m - b * l * m - d * i * n + a * l * n + b * i * p - a * j * p
            a11 = -d * f * m + b * h * m + d * e * n - a * h * n - b * e * p + a * f * p
            a12 = d * f * i - b * h * i - d * e * j + a * h * j + b * e * l - a * f * l
            a13 = g * j * m - f * k * m - g * i * n + e * k * n + f * i * o - e * j * o
            a14 = -c * j * m + b * k * m + c * i * n - a * k * n - b * i * o + a * j * o
            a15 = c * f * m - b * g * m - c * e * n + a * g * n + b * e * o - a * f * o
            a16 = -c * f * i + b * g * i + c * e * j - a * g * j - b * e * k + a * f * k

            if dt == 0:
                ans = "No Inverse"
                winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold", text=str(ans),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=168, width=320, x=470, y=237)

            else:
                ans1 = round(a1 / dt, 2)
                ans2 = round(a2 / dt, 2)
                ans3 = round(a3 / dt, 2)
                ans4 = round(a4 / dt, 2)
                ans5 = round(a5 / dt, 2)
                ans6 = round(a6 / dt, 2)
                ans7 = round(a7 / dt, 2)
                ans8 = round(a8 / dt, 2)
                ans9 = round(a9 / dt, 2)
                ans10 = round(a10 / dt, 2)
                ans11 = round(a11 / dt, 2)
                ans12 = round(a12 / dt, 2)
                ans13 = round(a13 / dt, 2)
                ans14 = round(a14 / dt, 2)
                ans15 = round(a15 / dt, 2)
                ans16 = round(a16 / dt, 2)
                winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
                OutputPlace = Label(top4dMatrix, font="Tahoma 13 bold",
                                    text="Inverse"+"\n"+"\n"+str(ans1) + "\t" + str(ans2) + "\t" + str(ans3) + "\t" + str(ans4) +
                                         "\n" + str(ans5) + "\t" + str(ans6) + "\t" + str(ans7) + "\t" + str(ans8) +
                                         "\n" + str(ans9) + "\t" + str(ans10) + "\t" + str(ans11) + "\t" + str(ans12) +
                                         "\n" + str(ans13) + "\t" + str(ans14) + "\t" + str(ans15) + "\t" + str(ans16),
                                    foreground="white", background="#030706")
                OutputPlace.place(height=168, width=320, x=470, y=237)

        matrixFOURd = PhotoImage(file="matrixFOURd.png")
        label = Label(top4dMatrix, image=matrixFOURd)
        label.image = matrixFOURd
        label.place(height=703, width=1251, x=0, y=0)

        block1 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block1.place(height=41, width=73, x=29, y=57)
        block2 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block2.place(height=41, width=73, x=116, y=57)
        block3 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block3.place(height=41, width=73, x=203, y=57)
        block4 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block4.place(height=41, width=73, x=291, y=57)
        block5 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block5.place(height=41, width=73, x=29, y=105)
        block6 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block6.place(height=41, width=73, x=116, y=105)
        block7 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block7.place(height=41, width=73, x=203, y=105)
        block8 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block8.place(height=41, width=73, x=291, y=105)
        block9 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block9.place(height=41, width=73, x=29, y=153)
        block10 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block10.place(height=41, width=73, x=116, y=153)
        block11 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block11.place(height=41, width=73, x=203, y=153)
        block12 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block12.place(height=41, width=73, x=291, y=153)
        block13 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block13.place(height=41, width=73, x=29, y=201)
        block14 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block14.place(height=41, width=73, x=116, y=201)
        block15 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block15.place(height=41, width=73, x=203, y=201)
        block16 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block16.place(height=41, width=73, x=291, y=201)
        block17 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block17.place(height=41, width=73, x=841, y=57)
        block18 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block18.place(height=41, width=73, x=929, y=57)
        block19 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block19.place(height=41, width=73, x=1017, y=57)
        block20 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block20.place(height=41, width=73, x=1105, y=57)
        block21 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block21.place(height=41, width=73, x=841, y=105)
        block22 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block22.place(height=41, width=73, x=929, y=105)
        block23 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block23.place(height=41, width=73, x=1017, y=105)
        block24 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block24.place(height=41, width=73, x=1105, y=105)
        block25 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block25.place(height=41, width=73, x=841, y=154)
        block26 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block26.place(height=41, width=73, x=929, y=154)
        block27 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block27.place(height=41, width=73, x=1017, y=154)
        block28 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block28.place(height=41, width=73, x=1105, y=154)
        block29 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block29.place(height=41, width=73, x=841, y=201)
        block30 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block30.place(height=41, width=73, x=929, y=201)
        block31 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block31.place(height=41, width=73, x=1017, y=201)
        block32 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block32.place(height=41, width=73, x=1105, y=201)
        block33 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block33.place(height=37, width=73, x=255, y=442)
        block35 = Entry(top4dMatrix, font="Tahoma", justify="center")
        block35.place(height=37, width=73, x=1048, y=444)

        def delete():
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block4.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            block7.delete(first=0, last=100)
            block8.delete(first=0, last=100)
            block9.delete(first=0, last=100)
            block10.delete(first=0, last=100)
            block11.delete(first=0, last=100)
            block12.delete(first=0, last=100)
            block13.delete(first=0, last=100)
            block14.delete(first=0, last=100)
            block15.delete(first=0, last=100)
            block16.delete(first=0, last=100)
            block17.delete(first=0, last=100)
            block18.delete(first=0, last=100)
            block19.delete(first=0, last=100)
            block20.delete(first=0, last=100)
            block21.delete(first=0, last=100)
            block22.delete(first=0, last=100)
            block23.delete(first=0, last=100)
            block24.delete(first=0, last=100)
            block25.delete(first=0, last=100)
            block26.delete(first=0, last=100)
            block27.delete(first=0, last=100)
            block28.delete(first=0, last=100)
            block29.delete(first=0, last=100)
            block30.delete(first=0, last=100)
            block31.delete(first=0, last=100)
            block32.delete(first=0, last=100)
            block33.delete(first=0, last=100)
            block35.delete(first=0, last=100)
            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)
            outputPlace = Label(top4dMatrix, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
            outputPlace.place(height=168, width=320, x=470, y=237)

        addButton = Button(top4dMatrix, font="Tahoma 15 bold", text="+", background="brown",
                           command=lambda: Addition(float(block1.get()), float(block2.get()), float(block3.get()),
                                                    float(block4.get()),
                                                    float(block5.get()), float(block6.get()), float(block7.get()),
                                                    float(block8.get()),
                                                    float(block9.get()), float(block10.get()), float(block11.get()),
                                                    float(block12.get()),
                                                    float(block13.get()), float(block14.get()), float(block15.get()),
                                                    float(block16.get()),
                                                    float(block17.get()), float(block18.get()), float(block19.get()),
                                                    float(block20.get()),
                                                    float(block21.get()), float(block22.get()), float(block23.get()),
                                                    float(block24.get()),
                                                    float(block25.get()), float(block26.get()), float(block27.get()),
                                                    float(block28.get()),
                                                    float(block29.get()), float(block30.get()), float(block31.get()),
                                                    float(block32.get())))
        addButton.place(height=51, width=55, x=479, y=119)
        minusButton = Button(top4dMatrix, font="Tahoma 15 bold", text="-", background="brown",
                             command=lambda: Subtraction(float(block1.get()), float(block2.get()), float(block3.get()),
                                                         float(block4.get()),
                                                         float(block5.get()), float(block6.get()), float(block7.get()),
                                                         float(block8.get()),
                                                         float(block9.get()), float(block10.get()),
                                                         float(block11.get()),
                                                         float(block12.get()),
                                                         float(block13.get()), float(block14.get()),
                                                         float(block15.get()),
                                                         float(block16.get()),
                                                         float(block17.get()), float(block18.get()),
                                                         float(block19.get()),
                                                         float(block20.get()),
                                                         float(block21.get()), float(block22.get()),
                                                         float(block23.get()),
                                                         float(block24.get()),
                                                         float(block25.get()), float(block26.get()),
                                                         float(block27.get()),
                                                         float(block28.get()),
                                                         float(block29.get()), float(block30.get()),
                                                         float(block31.get()),
                                                         float(block32.get())))
        minusButton.place(height=51, width=55, x=573, y=119)
        mulButton = Button(top4dMatrix, font="Tahoma 15 bold", text="x", background="brown",
                           command=lambda: Multiplication(float(block1.get()), float(block2.get()), float(block3.get()),
                                                          float(block4.get()),
                                                          float(block5.get()), float(block6.get()), float(block7.get()),
                                                          float(block8.get()),
                                                          float(block9.get()), float(block10.get()),
                                                          float(block11.get()),
                                                          float(block12.get()),
                                                          float(block13.get()), float(block14.get()),
                                                          float(block15.get()),
                                                          float(block16.get()),
                                                          float(block17.get()), float(block18.get()),
                                                          float(block19.get()),
                                                          float(block20.get()),
                                                          float(block21.get()), float(block22.get()),
                                                          float(block23.get()),
                                                          float(block24.get()),
                                                          float(block25.get()), float(block26.get()),
                                                          float(block27.get()),
                                                          float(block28.get()),
                                                          float(block29.get()), float(block30.get()),
                                                          float(block31.get()),
                                                          float(block32.get())))
        mulButton.place(height=51, width=55, x=665, y=119)

        inverButton1 = PhotoImage(file="inverseButton.png")
        label = Button(top4dMatrix, image=inverButton1,
                       command=lambda: InverseFirst(float(block1.get()), float(block2.get()),
                                                    float(block3.get()), float(block4.get()),
                                                    float(block5.get()), float(block6.get()),
                                                    float(block7.get()), float(block8.get()),
                                                    float(block9.get()), float(block10.get()),
                                                    float(block11.get()), float(block12.get()),
                                                    float(block13.get()), float(block14.get()),
                                                    float(block15.get()), float(block16.get())))
        label.image = inverButton1
        label.place(height=37, width=244, x=84, y=263)
        determinantButton1 = PhotoImage(file="determinantButton.png")
        label = Button(top4dMatrix, image=determinantButton1,
                       command=lambda: DeterminantFirst(float(block1.get()), float(block2.get()),
                                                        float(block3.get()), float(block4.get()),
                                                        float(block5.get()), float(block6.get()),
                                                        float(block7.get()), float(block8.get()),
                                                        float(block9.get()), float(block10.get()),
                                                        float(block11.get()), float(block12.get()),
                                                        float(block13.get()), float(block14.get()),
                                                        float(block15.get()), float(block16.get())))
        label.image = determinantButton1
        label.place(height=37, width=244, x=84, y=323)
        transposeButton1 = PhotoImage(file="transposeButton.png")
        label = Button(top4dMatrix, image=transposeButton1,
                       command=lambda: TransposeFirst(float(block1.get()), float(block2.get()),
                                                      float(block3.get()), float(block4.get()),
                                                      float(block5.get()), float(block6.get()),
                                                      float(block7.get()), float(block8.get()),
                                                      float(block9.get()), float(block10.get()),
                                                      float(block11.get()), float(block12.get()),
                                                      float(block13.get()), float(block14.get()),
                                                      float(block15.get()), float(block16.get())))
        label.image = transposeButton1
        label.place(height=37, width=244, x=84, y=383)
        multiplyByButton1 = PhotoImage(file="multiplyByButton.png")
        label = Button(top4dMatrix, image=multiplyByButton1,
                       command=lambda: MultiplybyFirst(float(block1.get()), float(block2.get()),
                                                       float(block3.get()), float(block4.get()),
                                                       float(block5.get()), float(block6.get()),
                                                       float(block7.get()), float(block8.get()),
                                                       float(block9.get()), float(block10.get()),
                                                       float(block11.get()), float(block12.get()),
                                                       float(block13.get()), float(block14.get()),
                                                       float(block15.get()), float(block16.get()),
                                                       float(block33.get())))
        label.image = multiplyByButton1
        label.place(height=37, width=171, x=84, y=442)

        inverButton2 = PhotoImage(file="inverseButton.png")
        label = Button(top4dMatrix, image=inverButton2,
                       command=lambda: InverseSecond(float(block17.get()), float(block18.get()),
                                                     float(block19.get()), float(block20.get()),
                                                     float(block21.get()), float(block22.get()),
                                                     float(block23.get()), float(block24.get()),
                                                     float(block25.get()), float(block26.get()),
                                                     float(block27.get()), float(block28.get()),
                                                     float(block29.get()), float(block30.get()),
                                                     float(block31.get()), float(block32.get())))
        label.image = inverButton2
        label.place(height=37, width=244, x=877, y=261)
        determinantButton2 = PhotoImage(file="determinantButton.png")
        label = Button(top4dMatrix, image=determinantButton2,
                       command=lambda: DeterminantSecond(float(block17.get()), float(block18.get()),
                                                         float(block19.get()), float(block20.get()),
                                                         float(block21.get()), float(block22.get()),
                                                         float(block23.get()), float(block24.get()),
                                                         float(block25.get()), float(block26.get()),
                                                         float(block27.get()), float(block28.get()),
                                                         float(block29.get()), float(block30.get()),
                                                         float(block31.get()), float(block32.get())))
        label.image = determinantButton2
        label.place(height=37, width=244, x=877, y=322)
        transposeButton2 = PhotoImage(file="transposeButton.png")
        label = Button(top4dMatrix, image=transposeButton2,
                       command=lambda: TransposeSecond(float(block17.get()), float(block18.get()),
                                                       float(block19.get()), float(block20.get()),
                                                       float(block21.get()), float(block22.get()),
                                                       float(block23.get()), float(block24.get()),
                                                       float(block25.get()), float(block26.get()),
                                                       float(block27.get()), float(block28.get()),
                                                       float(block29.get()), float(block30.get()),
                                                       float(block31.get()), float(block32.get())))
        label.image = transposeButton2
        label.place(height=37, width=244, x=877, y=383)
        multiplyByButton2 = PhotoImage(file="multiplyByButton.png")
        label = Button(top4dMatrix, image=multiplyByButton2,
                       command=lambda: MultiplybySecond(float(block17.get()), float(block18.get()),
                                                        float(block19.get()), float(block20.get()),
                                                        float(block21.get()), float(block22.get()),
                                                        float(block23.get()), float(block24.get()),
                                                        float(block25.get()), float(block26.get()),
                                                        float(block27.get()), float(block28.get()),
                                                        float(block29.get()), float(block30.get()),
                                                        float(block31.get()), float(block32.get()),
                                                        float(block35.get())))
        label.image = multiplyByButton2
        label.place(height=37, width=171, x=877, y=444)

        def open_info4dmatrix():
            topinfo4dmatrix = Toplevel()
            topinfo4dmatrix.title("4D Matrix Calculator")
            topinfo4dmatrix.geometry("1251x703+120+50")
            top4dMatrix.withdraw()

            winsound.PlaySound("noppl.wav", winsound.SND_ASYNC)

            info4dmatrix = PhotoImage(file="info4dmatrix.png")
            label = Label(topinfo4dmatrix, image=info4dmatrix)
            label.image = info4dmatrix
            label.place(height=703, width=1251, x=0, y=0)

            closeButton = PhotoImage(file="closeButton.png")
            label = Button(topinfo4dmatrix, image=closeButton, command=lambda: (top4dMatrix.deiconify(), topinfo4dmatrix.destroy()))
            label.image = closeButton
            label.place(height=66, width=70, x=1172, y=410)

        infoButton = PhotoImage(file="infoButton.png")
        label = Button(top4dMatrix, image=infoButton, command=open_info4dmatrix)
        label.image = infoButton
        label.place(height=66, width=70, x=1172, y=410)
        ResetButton = PhotoImage(file="ResetButton.png")
        label = Button(top4dMatrix, image=ResetButton, command=delete)
        label.image = ResetButton
        label.place(height=66, width=70, x=1172, y=483)
        BackButton = PhotoImage(file="BackButton.png")
        label = Button(top4dMatrix, image=BackButton,
                       command=lambda: (topMatrixMenu.deiconify(), top4dMatrix.destroy()))
        label.image = BackButton
        label.place(height=66, width=70, x=1172, y=556)
        ExitButton = PhotoImage(file="ExitButton.png")
        label = Button(top4dMatrix, image=ExitButton, command=lambda: closeprogram())
        label.image = ExitButton
        label.place(height=66, width=70, x=1172, y=629)

        OutputPlace = Label(top4dMatrix, font="Tahoma 15 bold", text=" ", foreground="white", background="#030706")
        OutputPlace.place(height=168, width=320, x=470, y=237)

    buttonMatrix2d = PhotoImage(file="buttonmatrix2d.png")
    label = Button(topMatrixMenu, image=buttonMatrix2d, command=open2dMatrix)
    label.image = buttonMatrix2d
    label.place(height=64, width=355, x=448, y=339)
    button2dtrans = PhotoImage(file="button2dtrans.png")
    label = Button(topMatrixMenu, image=button2dtrans, command=open2dTrans)
    label.image = button2dtrans
    label.place(height=64, width=355, x=448, y=427)
    buttonMatrix3d = PhotoImage(file="buttonmatrix3d.png")
    label = Button(topMatrixMenu, image=buttonMatrix3d, command=open3dMatrix)
    label.image = buttonMatrix3d
    label.place(height=64, width=355, x=448, y=515)
    buttonMatrix4d = PhotoImage(file="buttonmatrix4d.png")
    label = Button(topMatrixMenu, image=buttonMatrix4d, command=open4dMatrix)
    label.image = buttonMatrix4d
    label.place(height=64, width=355, x=448, y=603)

    BackButton = PhotoImage(file="BackButton.png")
    label = Button(topMatrixMenu, image=BackButton, command=lambda: (root.deiconify(), topMatrixMenu.destroy()))
    label.image = BackButton
    label.place(height=66, width=70, x=1172, y=556)
    ExitButton = PhotoImage(file="ExitButton.png")
    label = Button(topMatrixMenu, image=ExitButton, command=lambda: closeprogram())
    label.image = ExitButton
    label.place(height=66, width=70, x=1172, y=629)

def opengram():
    global dim
    topgram = Toplevel()
    topgram.title("Gram Schmidt Calculator")
    topgram.geometry("1251x703+120+50")
    root.withdraw()

    winsound.PlaySound("zombie.wav", winsound.SND_ASYNC)

    gram = PhotoImage(file="gram.png")
    label = Label(topgram, image=gram)
    label.image = gram
    label.place(height=703, width=1251, x=0, y=0)

    block1 = Entry(topgram, font="Tahoma", justify="center")
    block1.place(height=40, width=90, x=358, y=72)
    block2 = Entry(topgram, font="Tahoma", justify="center")
    block2.place(height=40, width=90, x=461, y=72)
    block3 = Entry(topgram, font="Tahoma", justify="center")
    block3.place(height=40, width=90, x=564, y=72)
    block4 = Entry(topgram, font="Tahoma", justify="center")
    block4.place(height=40, width=90, x=667, y=72)
    block5 = Entry(topgram, font="Tahoma", justify="center")
    block5.place(height=40, width=90, x=358, y=128)
    block6 = Entry(topgram, font="Tahoma", justify="center")
    block6.place(height=40, width=90, x=461, y=128)
    block7 = Entry(topgram, font="Tahoma", justify="center")
    block7.place(height=40, width=90, x=564, y=128)
    block8 = Entry(topgram, font="Tahoma", justify="center")
    block8.place(height=40, width=90, x=667, y=128)
    block9 = Entry(topgram, font="Tahoma", justify="center")
    block9.place(height=40, width=90, x=358, y=184)
    block10 = Entry(topgram, font="Tahoma", justify="center")
    block10.place(height=40, width=90, x=461, y=184)
    block11 = Entry(topgram, font="Tahoma", justify="center")
    block11.place(height=40, width=90, x=564, y=184)
    block12 = Entry(topgram, font="Tahoma", justify="center")
    block12.place(height=40, width=90, x=667, y=184)
    block13 = Entry(topgram, font="Tahoma", justify="center")
    block13.place(height=40, width=90, x=358, y=240)
    block14 = Entry(topgram, font="Tahoma", justify="center")
    block14.place(height=40, width=90, x=461, y=240)
    block15 = Entry(topgram, font="Tahoma", justify="center")
    block15.place(height=40, width=90, x=564, y=240)
    block16 = Entry(topgram, font="Tahoma", justify="center")
    block16.place(height=40, width=90, x=667, y=240)
    def alllow():
        all = (block1, block2, block3, block4, block5, block6, block7, block8, block9, block10,
               block11, block12, block13, block14, block15, block16)
        for i in range(16):
            all[i].lower()
    alllow()

    def block2x2():
        global dim
        dim = 2
        winsound.PlaySound("zombiebreath1.wav", winsound.SND_ASYNC)
        alllow()
        all = (block1, block2, block5, block6)
        for i in range(4):
            all[i].lift()

    def block3x3():
        global dim
        dim = 3
        winsound.PlaySound("zombiebreath2.wav", winsound.SND_ASYNC)
        alllow()
        all = (block1, block2, block3, block5, block6, block7, block9, block10, block11)
        for i in range(9):
            all[i].lift()

    def block4x4():
        global dim
        dim = 4
        winsound.PlaySound("zombiebreath3.wav", winsound.SND_ASYNC)
        alllow()
        all = (block1, block2, block3, block4, block5, block6, block7, block8, block9, block10,
               block11, block12, block13, block14, block15, block16)
        for i in range(16):
            all[i].lift()

    def calculate():
        winsound.PlaySound("zombiebite.wav", winsound.SND_ASYNC)
        global dim
        if dim == 2 :
            num1 = float(block1.get())
            num2 = float(block2.get())
            num3 = float(block5.get())
            num4 = float(block6.get())
            num11 = num1**2
            num22 = num2**2
            k1 = math.sqrt(num11+num22)
            if k1 == 0 :
                OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                    text="Invalid Input", foreground="#39c8a4", background="#020202")
                OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
            else :
                e1ans1 = num1/k1
                e1ans2 = num2/k1
                finalans1 = (round(e1ans1, 2), round(e1ans2, 2))
                v2e1 = num3*e1ans1 + num4*e1ans2
                u2ans1 = num3 - (v2e1*e1ans1)
                u2ans2 = num4 - (v2e1*e1ans2)
                num33 = u2ans1**2
                num44 = u2ans2**2
                k2 = math.sqrt(num33+num44)
                if k2 == 0 :
                    OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                        text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1),
                                        foreground="#39c8a4", background="#020202")
                    OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
                else :
                    e2ans1 = num3/k2
                    e2ans2 = num4/k2
                    finalans2 = (round(e2ans1,2), round(e2ans2,2))
                    OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                        text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1) + "\n"
                                             + "e2 = " + str(finalans2),
                                        foreground="#39c8a4", background="#020202")
                    OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

        if dim == 3 :
            num1 = float(block1.get())
            num2 = float(block2.get())
            num3 = float(block3.get())
            num4 = float(block5.get())
            num5 = float(block6.get())
            num6 = float(block7.get())
            num7 = float(block9.get())
            num8 = float(block10.get())
            num9 = float(block11.get())
            num11 = num1 ** 2
            num22 = num2 ** 2
            num33 = num3 ** 2
            k1 = math.sqrt(num11 + num22 + num33)
            if k1 == 0 :
                OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                   text="Invalid Input", foreground="#39c8a4", background="#020202")
                OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
            else :
                e1ans1 = num1 / k1
                e1ans2 = num2 / k1
                e1ans3 = num3 / k1
                finalans1 = (round(e1ans1, 2), round(e1ans2, 2), round(e1ans3, 2))
                v2e1 = num4*e1ans1 + num5*e1ans2 + num6*e1ans3
                u2ans1 = num4 - (v2e1 * e1ans1)
                u2ans2 = num5 - (v2e1 * e1ans2)
                u2ans3 = num6 - (v2e1 * e1ans3)
                num44 = u2ans1 ** 2
                num55 = u2ans2 ** 2
                num66 = u2ans3 ** 2
                k2 = math.sqrt(num44 + num55 + num66)
                if k2 == 0 :
                    OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                        text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1),
                                        foreground="#39c8a4", background="#020202")
                    OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
                else :
                    e2ans1 = num4 / k2
                    e2ans2 = num5 / k2
                    e2ans3 = num6 / k2
                    finalans2 = (round(e2ans1, 2), round(e2ans2, 2), round(e2ans3, 2))
                    v3e1 = num7*e1ans1 + num8*e1ans2 + num9*e1ans3
                    v3e2 = num7*e2ans1 + num8*e2ans2 + num9*e2ans3
                    u3ans1 = num7 - (v3e1 * e1ans1) - (v3e2 * e2ans1)
                    u3ans2 = num8 - (v3e1 * e1ans2) - (v3e2 * e2ans2)
                    u3ans3 = num9 - (v3e1 * e1ans3) - (v3e2 * e2ans3)
                    num77 = u3ans1 ** 2
                    num88 = u3ans2 ** 2
                    num99 = u3ans3 ** 2
                    k3 = math.sqrt(num77 + num88 + num99)
                    if k3 == 0 :
                        OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                            text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1)
                                                 + "\n" + "e2 = " + str(finalans2),
                                            foreground="#39c8a4", background="#020202")
                        OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
                    else :
                        e3ans1 = num7 / k3
                        e3ans2 = num8 / k3
                        e3ans3 = num9 / k3
                        finalans3 = (round(e3ans1, 2), round(e3ans2, 2), round(e3ans3, 2))
                        OutputPlace = Label(topgram, font="Tahoma 13 bold",
                                           text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1) + "\n" + "e2 = "
                                                + str(finalans2) + "\n" + "e3 = " + str(finalans3),
                                           foreground="#39c8a4", background="#020202")
                        OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

        if dim == 4 :
            num1 = float(block1.get())
            num2 = float(block2.get())
            num3 = float(block3.get())
            num4 = float(block4.get())
            num5 = float(block5.get())
            num6 = float(block6.get())
            num7 = float(block7.get())
            num8 = float(block8.get())
            num9 = float(block9.get())
            num10 = float(block10.get())
            num11 = float(block11.get())
            num12 = float(block12.get())
            num13 = float(block13.get())
            num14 = float(block14.get())
            num15 = float(block15.get())
            num16 = float(block16.get())
            numa = num1 ** 2
            numb = num2 ** 2
            numc = num3 ** 2
            numd = num4 ** 2
            k1 = math.sqrt(numa + numb + numc + numd)
            if k1 == 0 :
                OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                   text="Invalid Input", foreground="#39c8a4", background="#020202")
                OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
            else :
                e1ans1 = num1 / k1
                e1ans2 = num2 / k1
                e1ans3 = num3 / k1
                e1ans4 = num4 / k1
                finalans1 = (round(e1ans1, 2), round(e1ans2, 2), round(e1ans3, 2), round(e1ans4, 2))
                v2e1 = num5*e1ans1 + num6*e1ans2 + num7*e1ans3 + num8*e1ans4
                u2ans1 = num5 - (v2e1 * e1ans1)
                u2ans2 = num6 - (v2e1 * e1ans2)
                u2ans3 = num7 - (v2e1 * e1ans3)
                u2ans4 = num8 - (v2e1 * e1ans4)
                num55 = u2ans1 ** 2
                num66 = u2ans2 ** 2
                num77 = u2ans3 ** 2
                num88 = u2ans4 ** 2
                k2 = math.sqrt(num55 + num66 + num77 + num88)
                if k2 == 0 :
                    OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                        text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1),
                                        foreground="#39c8a4", background="#020202")
                    OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
                else :
                    e2ans1 = num5 / k2
                    e2ans2 = num6 / k2
                    e2ans3 = num7 / k2
                    e2ans4 = num8 / k2
                    finalans2 = (round(e2ans1, 2), round(e2ans2, 2), round(e2ans3, 2), round(e2ans4, 2))
                    v3e1 = num9*e1ans1 + num10*e1ans2 + num11*e1ans3 + num12*e1ans4
                    v3e2 = num9*e2ans1 + num10*e2ans2 + num11*e2ans3 + num12*e2ans4
                    u3ans1 = num9 - (v3e1 * e1ans1) - (v3e2 * e2ans1)
                    u3ans2 = num10 - (v3e1 * e1ans2) - (v3e2 * e2ans2)
                    u3ans3 = num11 - (v3e1 * e1ans3) - (v3e2 * e2ans3)
                    u3ans4 = num12 - (v3e1 * e1ans4) - (v3e2 * e2ans4)
                    num99 = u3ans1 ** 2
                    num1010 = u3ans2 ** 2
                    num1111 = u3ans3 ** 2
                    num1212 = u3ans4 ** 2
                    k3 = math.sqrt(num99 + num1010 + num1111 + num1212)
                    if k3 == 0 :
                        OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                            text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1)
                                                 + "\n" + "e2 = " + str(finalans2),
                                            foreground="#39c8a4", background="#020202")
                        OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
                    else :
                        e3ans1 = num9 / k3
                        e3ans2 = num10 / k3
                        e3ans3 = num11 / k3
                        e3ans4 = num12 / k3
                        finalans3 = (round(e3ans1, 2), round(e3ans2, 2), round(e3ans3, 2), round(e3ans4, 2))
                        v4e1 = num13 * e1ans1 + num14 * e1ans2 + num15 * e1ans3 + num16 * e1ans4
                        v4e2 = num13 * e2ans1 + num14 * e2ans2 + num15 * e2ans3 + num16 * e2ans4
                        v4e3 = num13 * e3ans1 + num14 * e3ans2 + num15 * e3ans3 + num16 * e3ans4
                        u4ans1 = num9 - (v4e1 * e1ans1) - (v4e2 * e2ans1) - (v4e3 * e3ans1)
                        u4ans2 = num10 - (v4e1 * e1ans2) - (v4e2 * e2ans2) - (v4e3 * e3ans2)
                        u4ans3 = num11 - (v4e1 * e1ans3) - (v4e2 * e2ans3) - (v4e3 * e3ans3)
                        u4ans4 = num12 - (v4e1 * e1ans4) - (v4e2 * e2ans4) - (v4e3 * e3ans4)
                        num1313 = u4ans1 ** 2
                        num1414 = u4ans2 ** 2
                        num1515 = u4ans3 ** 2
                        num1616 = u4ans4 ** 2
                        k4 = math.sqrt(num1313 + num1414 + num1515 + num1616)
                        if k4 == 0 :
                            OutputPlace = Label(topgram, font="Tahoma 15 bold",
                                                text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1)
                                                     + "\n" + "e2 = " + str(finalans2)
                                                     + "\n" + "e3 = " + str(finalans3),
                                                foreground="#39c8a4", background="#020202")
                            OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)
                        else :
                            e4ans1 = num13 / k4
                            e4ans2 = num14 / k4
                            e4ans3 = num15 / k4
                            e4ans4 = num16 / k4
                            finalans4 = (round(e4ans1, 2), round(e4ans2, 2), round(e4ans3, 2), round(e4ans4, 2))
                            OutputPlace = Label(topgram, font="Tahoma 13 bold",
                                                text="Answer" + "\n" + "\n" + "e1 = " + str(finalans1)
                                                     + "\n" + "e2 = " + str(finalans2)
                                                     + "\n" + "e3 = " + str(finalans3)
                                                     + "\n" + "e4 = " + str(finalans4),
                                                foreground="#39c8a4", background="#020202")
                            OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

    def delete():
        winsound.PlaySound("zombiebite.wav", winsound.SND_ASYNC)
        global dim
        if dim == 4 :
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block4.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            block7.delete(first=0, last=100)
            block8.delete(first=0, last=100)
            block9.delete(first=0, last=100)
            block10.delete(first=0, last=100)
            block11.delete(first=0, last=100)
            block12.delete(first=0, last=100)
            block13.delete(first=0, last=100)
            block14.delete(first=0, last=100)
            block15.delete(first=0, last=100)
            block16.delete(first=0, last=100)
            OutputPlace = Label(topgram, text=" ", background="#020202")
            OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

        if dim == 3:
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block3.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            block7.delete(first=0, last=100)
            block9.delete(first=0, last=100)
            block10.delete(first=0, last=100)
            block11.delete(first=0, last=100)
            OutputPlace = Label(topgram, text=" ", background="#020202")
            OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

        if dim == 2:
            block1.delete(first=0, last=100)
            block2.delete(first=0, last=100)
            block5.delete(first=0, last=100)
            block6.delete(first=0, last=100)
            OutputPlace = Label(topgram, text=" ", background="#020202")
            OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

    button2vector = PhotoImage(file="button2vector.png")
    label = Button(topgram, image=button2vector, command=block2x2)
    label.image = button2vector
    label.place(height=50, width=206, x=52, y=168)
    button3vector = PhotoImage(file="button3vector.png")
    label = Button(topgram, image=button3vector, command=block3x3)
    label.image = button3vector
    label.place(height=50, width=206, x=52, y=251)
    button4vector = PhotoImage(file="button4vector.png")
    label = Button(topgram, image=button4vector, command=block4x4)
    label.image = button4vector
    label.place(height=50, width=206, x=52, y=332)
    calbutton = Button(topgram, text="Calculate", font="Tahoma 20 bold", background="darkred", command=calculate)
    calbutton.place(height=50, width=206, x=442, y=332)

    def open_infogram():
        topinfogram = Toplevel()
        topinfogram.title("Gram Schmidt Calculator")
        topinfogram.geometry("1251x703+120+50")
        topgram.withdraw()

        winsound.PlaySound("zombiebreath4.wav", winsound.SND_ASYNC)

        infogram = PhotoImage(file="infogram.png")
        label = Label(topinfogram, image=infogram)
        label.image = infogram
        label.place(height=703, width=1251, x=0, y=0)

        closeButton = PhotoImage(file="closeButton.png")
        label = Button(topinfogram, image=closeButton,
                       command=lambda: (topgram.deiconify(), topinfogram.destroy()))
        label.image = closeButton
        label.place(height=66, width=70, x=1172, y=410)

    infoButton = PhotoImage(file="infoButton.png")
    label = Button(topgram, image=infoButton, command=open_infogram)
    label.image = infoButton
    label.place(height=66, width=70, x=1172, y=410)
    ResetButton = PhotoImage(file="ResetButton.png")
    label = Button(topgram, image=ResetButton, command=delete)
    label.image = ResetButton
    label.place(height=66, width=70, x=1172, y=483)
    BackButton = PhotoImage(file="BackButton.png")
    label = Button(topgram, image=BackButton, command=lambda: (root.deiconify(), topgram.destroy()))
    label.image = BackButton
    label.place(height=66, width=70, x=1172, y=556)
    ExitButton = PhotoImage(file="ExitButton.png")
    label = Button(topgram, image=ExitButton, command=lambda: closeprogram())
    label.image = ExitButton
    label.place(height=66, width=70, x=1172, y=629)

    OutputPlace = Label(topgram, text=" ", background="#020202")
    OutputPlace.place(height=207.43, width=349.95, x=852.13, y=45.53)

def openeuler():
    topeuler = Toplevel()
    topeuler.title("Euler Calculator")
    topeuler.geometry("1251x703+120+50")
    root.withdraw()

    winsound.PlaySound("piano1.wav", winsound.SND_ASYNC)

    euler = PhotoImage(file="euler.png")
    label = Label(topeuler, image=euler)
    label.image = euler
    label.place(height=703, width=1251, x=0, y=0)

    block1 = Entry(topeuler, font="Tahoma 15 bold", justify="center")
    block1.place(height=45, width=381, x=282, y=37)
    block2 = Entry(topeuler, font="Tahoma 15 bold", justify="center")
    block2.place(height=45, width=90, x=282, y=103)
    block3 = Entry(topeuler, font="Tahoma 15 bold", justify="center")
    block3.place(height=45, width=90, x=132, y=173)
    block4 = Entry(topeuler, font="Tahoma 15 bold", justify="center")
    block4.place(height=45, width=90, x=282, y=173)
    block5 = Entry(topeuler, font="Tahoma 15 bold", justify="center")
    block5.place(height=45, width=90, x=282, y=243)

    def calculate():
        winsound.PlaySound("piano2.wav", winsound.SND_ASYNC)
        X = []
        Y = []
        function = block1.get()
        function = function.replace("abs", "math.abs")
        function = function.replace("sqrt", "math.sqrt")
        function = function.replace("^", "**")
        function = function.replace("pi", "math.pi")
        function = function.replace("e", "math.e")
        function = function.replace("log", "math.log10")
        function = function.replace("ln", "math.log")
        function = function.replace("sin", "math.sin")
        function = function.replace("cos", "math.cos")
        function = function.replace("tan", "math.tan")
        function = function.replace("cot", "1/math.tan")
        function = function.replace("sec", "1/math.cos")
        function = function.replace("csc", "1/math.sin")
        function = function.replace("asin", "math.asin")
        function = function.replace("acos", "math.acos")
        function = function.replace("atan", "math.atan")
        h = float(block2.get())
        x = float(block3.get())
        y = float(block4.get())
        max = float(block5.get())
        b = int((max - x) / h)
        X.append(x)
        Y.append(y)
        for i in range(b):
            y = y + h * (eval(function))
            x = x + h
            X.append(x)
            Y.append(round(y, 5))
        xlabel = str(np.array(X).reshape(b + 1, 1)).replace('[[', ' ').replace('[', '').replace(']', '').replace(']]', '')
        ylabel = str(np.array(Y).reshape(b + 1, 1)).replace('[[', ' ').replace('[', '').replace(']', '').replace(']]', '')
        OutputPlace1 = Label(topeuler, font="Tahoma 13 bold", text=xlabel, background="#f9a4fc", anchor="n")
        OutputPlace1.place(height=416, width=61, x=884, y=57.99)
        OutputPlace2 = Label(topeuler, font="Tahoma 13 bold", text=ylabel, background="#f9a4fc", anchor="n")
        OutputPlace2.place(height=416, width=168, x=951, y=58)

        plt.plot(X,Y)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("Graph of " + function)
        plt.show()

    calbutton = Button(topeuler, text="Calculate", font="Tahoma 20 bold", background="pink", command=calculate)
    calbutton.place(height=50, width=282, x=147, y=327)

    def open_infoeuler():
        topinfoeuler = Toplevel()
        topinfoeuler.title("Euler Calculator")
        topinfoeuler.geometry("1251x703+120+50")
        topeuler.withdraw()

        winsound.PlaySound("piano3.wav", winsound.SND_ASYNC)

        infoeuler = PhotoImage(file="infoeuler.png")
        label = Label(topinfoeuler, image=infoeuler)
        label.image = infoeuler
        label.place(height=703, width=1251, x=0, y=0)

        closeButton = PhotoImage(file="closeButton.png")
        label = Button(topinfoeuler, image=closeButton,
                       command=lambda: (topeuler.deiconify(), topinfoeuler.destroy()))
        label.image = closeButton
        label.place(height=66, width=70, x=1172, y=410)

    def delete():
        block1.delete(first=0, last=100)
        block2.delete(first=0, last=100)
        block3.delete(first=0, last=100)
        block4.delete(first=0, last=100)
        block5.delete(first=0, last=100)
        OutputPlace1 = Label(topeuler, font="Tahoma 10 bold", text=" ", background="#f9a4fc")
        OutputPlace1.place(height=416, width=61, x=884, y=57.99)
        OutputPlace2 = Label(topeuler, font="Tahoma 10 bold", text=" ", background="#f9a4fc")
        OutputPlace2.place(height=416, width=168, x=951, y=58)

    infoButton = PhotoImage(file="infoButton.png")
    label = Button(topeuler, image=infoButton, command=open_infoeuler)
    label.image = infoButton
    label.place(height=66, width=70, x=1172, y=410)
    ResetButton = PhotoImage(file="ResetButton.png")
    label = Button(topeuler, image=ResetButton, command=delete)
    label.image = ResetButton
    label.place(height=66, width=70, x=1172, y=483)
    BackButton = PhotoImage(file="BackButton.png")
    label = Button(topeuler, image=BackButton, command=lambda: (root.deiconify(), topeuler.destroy()))
    label.image = BackButton
    label.place(height=66, width=70, x=1172, y=556)
    ExitButton = PhotoImage(file="ExitButton.png")
    label = Button(topeuler, image=ExitButton, command=lambda: closeprogram())
    label.image = ExitButton
    label.place(height=66, width=70, x=1172, y=629)

    OutputPlace1 = Label(topeuler, font="Tahoma 10 bold", text=" ", background="#f9a4fc")
    OutputPlace1.place(height=416, width=61, x=884, y=57.99)
    OutputPlace2 = Label(topeuler, font="Tahoma 10 bold", text=" ", background="#f9a4fc")
    OutputPlace2.place(height=416, width=168, x=951, y=58)

def closeprogram():
    msg = tk.messagebox.askyesno("Exit", "Are you sure?")
    if (msg):
        exit()

root = Tk()
winsound.PlaySound("yay.wav", winsound.SND_ASYNC)

mcgMainMenu = PhotoImage(file="mcgMainMenu.png")
label = Label(root, image=mcgMainMenu)
label.image = mcgMainMenu
label.place(height=703, width=1251, x=0, y=0)

vectorButton = PhotoImage(file="vectorButton.png")
label = Button(root, image=vectorButton, command=openvectorMenu)
label.image=vectorButton
label.place(height=316, width=591, x=0, y=0)
matrixButton = PhotoImage(file="matrixButton.png")
label = Button(root, image=matrixButton, command=openmatrixMenu)
label.image=matrixButton
label.place(height=316, width=591, x=660, y=0)
gramSchmidtButton = PhotoImage(file="gramSchmidtButton.png")
label = Button(root, image=gramSchmidtButton, command=opengram)
label.image=gramSchmidtButton
label.place(height=316, width=591, x=0, y=386)
eulerButton = PhotoImage(file="eulerButton.png")
label = Button(root, image=eulerButton, command=openeuler)
label.image=eulerButton
label.place(height=316, width=591, x=660, y=386)

root.title("Calculator")
root.geometry("1251x703+120+50")
root.mainloop()
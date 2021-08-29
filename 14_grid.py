# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 그리드 : 일종의 격자. 격자 안에 다양한 위젯들을 배치
# pack은 쌓는 느낌이라고 한다면, 그리드는 지정된 좌표에 집어넣는다는 느낌

#btn1 = Button(root, text="버튼1")
#btn2 = Button(root, text="버튼2")

# 그리드를 선언할 떄는 행과 열 값을 입력
#btn1.grid(row=0, column=0)
#btn2.grid(row=1, column=1)

# 크기 조절 -> padx, pady

# 맨 윗줄
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

# grid의 sticky 속성
# 지정한 방향으로 위젯을 달라붙게 하는 속성
# 예) sticky=N+E+W+S

# grid의 padx, pady 속성
# 그리드의 요소들 사이의 간격 지정 가능

btn_f16.grid(row=0, column=0, sticky=N+W+E+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+W+E+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+W+E+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+W+E+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+W+E+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+W+E+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+W+E+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+W+E+S, padx=3, pady=3)

# 7 시작 줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+W+E+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+W+E+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+W+E+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+W+E+S, padx=3, pady=3)

# 4 시작 줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+W+E+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+W+E+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+W+E+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+W+E+S, padx=3, pady=3)

# 1 시작 줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2) # 세로로 합쳐짐

btn_1.grid(row=4, column=0, sticky=N+W+E+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+W+E+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+W+E+S, padx=3, pady=3)
# rowspan=n : 행 n개를 합침
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+W+E+S, padx=3, pady=3) # 현재 위치로부터 아래쪽으로 두 줄을 합침

# 0 시작 줄
btn_0 = Button(root, text="0", width=5, height=2) # 가로로 합쳐짐
btn_point = Button(root, text=".", width=5, height=2)

# columnspan=n : 열 n개를 합침
btn_0.grid(row=5, column=0, columnspan=2, sticky=N+W+E+S, padx=3, pady=3) # 현재 위치로부터 오른쪽으로 두 줄을 합침
btn_point.grid(row=5, column=2, sticky=N+W+E+S, padx=3, pady=3)

root.mainloop() # 창이 닫히지 않도록 루프 돌림
# tkinter -> 윈도우 모듈
from tkinter import *
import tkinter.ttk as ttk # 프로그레스 바는 tikinter.ttk에 있다
import time

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정


# 프로그레스 바 : 진행 상황을 표시해줌
# maximum : 최댓값
# mode : indeterminate(언제 끝날 지 모름), determinate(결정됨. 처음부터 끝까지 점점 차는 형태)
# progressBar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
"""
progressBar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressBar.start(10) # start 함수 : 프로그레스 바가 실행됨. 10ms마다 움직임
progressBar.pack()

def btncmd():
    progressBar.stop() # 프로그레스 바 작동 중지

btn1 = Button(root, text="중지", command=btncmd)
btn1.pack()
"""

# length : 프로그레스 바의 길이
# variable : 프로그레스 바와 연동할 변수
p_var2 = DoubleVar() # double형 변수 선언
progressBar2 = ttk.Progressbar(root, maximum=100, mode="determinate", length=150, variable=p_var2)
progressBar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar 값 설정
        progressBar2.update() # UI 업데이트
        print(i)

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림
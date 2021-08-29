# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 체크박스(체크, 체크해제를 할 수 있는 위젯)
# Checkbutton 클래스에는 꼭 variable을 적어주어야 한다. (variable : 체크박스의 상태에 따라 달라질 변수)

# IntVar() : 정수형 변수를 선언할 때 사용 가능
# StringVar() : 문자형 변수를 선언할 때 사용 가능

chkvar = IntVar() # chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)

# 스크립트에서 체크박스 조작하기
# chkbox.select() # 선택 처리
# chkbox.deselect() # 선택 해제 처리

chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn1 = Button(root, text="클릭", command=btncmd)
btn1.pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림
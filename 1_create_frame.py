# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정
# root.geometry("640x480+1000+400") # 가로x세로+x좌표+y좌표. 띄어쓰기 하면 안 됨

# root.resizable(False, False) # x, y 값 변경 불가능 (창 크기 변경 x) & 최대화 버튼 비활성화

root.mainloop() # 창이 닫히지 않도록 루프 돌림
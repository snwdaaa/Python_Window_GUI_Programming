# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 프레임 : 여러 위젯들을 묶어 관리를 용이하게 하는 테두리

# relief : 테두리 모양
# bd : 외곽선
frame_burger = Frame(root, relief="solid", bd=1)
# side : 어느 쪽 위치에 놓을 지
# fill : both(위 아래 꽉 채움)
# expand : 확장
frame_burger.pack(side="left", fill="both", expand=True)

# 버튼을 프레임 안에 포함 
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# LabelFrame : 제목이 있는 프레임
frame_beverage = LabelFrame(root, text="음료")
frame_beverage.pack(side="right", fill="both", expand=True)

Button(frame_beverage, text="콜라").pack()
Button(frame_beverage, text="사이다").pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림
# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 스크롤 바
# 스크롤 바와 스크롤이 되는 대상을 한 프레임 안에 넣는 것이 관리가 편함
# 스크롤 바와 스크롤이 되는 대상을 각각 서로를 연결시켜주는 것이 중요

frame = Frame(root)
frame.pack()

# 스크롤 바
scrollBar = Scrollbar(frame)
scrollBar.pack(side="right", fill="y") # 스크롤 바가 프레임의 맨 오른쪽에 붙고, 위아래로 채워지게 만듬

# 리스트 박스
# yscrollcommand : y축으로 스크롤하는데 필요한 스크롤바 변수를 대입
# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollBar.set) # (중요)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack()

# 스크롤 바의 command를 리스트 박스의 yview로 맵핑
scrollBar.config(command=listbox.yview) # (중요)

root.mainloop() # 창이 닫히지 않도록 루프 돌림
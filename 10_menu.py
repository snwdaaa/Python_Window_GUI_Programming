# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 메뉴 : 프로그램 창 상단에 있는 바

menu = Menu(root) # 메뉴 인스턴스 선언 후

def create_new_file():
    print("새 파일을 만듭니다.")

# File 메뉴

# tearoff : 
menu_file = Menu(menu, tearoff=0) # 부모가 root가 아닌 메뉴 바
# add_command : label로 표시. 누르면 command 실행
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
# 구분자(가로 구분선) 추가
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
# state 매개변수 : 비활성화(disable)
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

# add_cascade : 메뉴 바에 menu_file을 추가하고, 이름을 "File"로 설정
menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="Edit")

# Language 메뉴 (radio 버튼을 통해 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")

menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 (체크 박스)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

def btncmd():
    pass

btn1 = Button(root, text="시작", command=btncmd)
btn1.pack()

root.config(menu=menu) # root의 config에서 menu 매개변수 설정
root.mainloop() # 창이 닫히지 않도록 루프 돌림
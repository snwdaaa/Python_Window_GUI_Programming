# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 텍스트 입력창 (텍스트 위젯)
txt = Text(root, width=30, height=5)
txt.pack()

# insert : 기본값으로 글자를 미리 추가
# insert(index, chars) : index에 chars 추가
txt.insert(END, "글자를 입력하세요") # 힌트 텍스트 or 기본값 제공 등으로 사용 가능

# 엔트리
# 텍스트와 차이 : 아이디 입력처럼 한 줄만 입력받음. 줄바꿈이 불가능하게 만들 때 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요") # index 0부터

def btncmd():
    print(txt.get("1.0", END)) # "1.0"(1번줄의 0번째 column 위치부터) END(끝까지) 있는 모든 텍스트를 가져옴
    print(e.get()) # entry는 get 함수에 인수 필요 X

    txt.delete("1.0", END) # 텍스트 삭제
    e.delete(0, END) # 처음부터 끝까지 텍스트 삭제

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림
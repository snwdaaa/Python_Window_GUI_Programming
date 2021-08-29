# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 리스트 박스 : 여러 줄에 걸쳐서 목록을 관리하는 위젯
listbox = Listbox(root, selectmode="extended", height=0) # Listbox, selectmode
# selectmode : extended(한 개 이상 선택 가능), single(하나만 선택 가능)
# 리스트 박스의 height가 0이면 다 보여주는데, 다른 숫자면 그 숫자만큼만 보여줌
listbox.insert(0, "사과") # insert(인덱스, 값)
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # 인덱스를 END로 하면 계속 마지막에 추가됨
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 리스트 박스에서 맨 마지막 항목 삭제
    # listbox.delete(END)
    # 리스트 박스에서 맨 첫 번째 항목 삭제
    # listbox.delete(0)

    # 갯수 확인
    print("리스트에는 ", listbox.size(), "개가 있어요") # size() 리스트 박스의 요소의 개수 리턴

    # 항목 확인
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2)) # get(a, b) : a-1번째부터 b-1번째까지 리스트에 있는 값 출력

    # 선택된 항목 확인 (위치로 반환)
    print("현재 선택된 항목은 ", listbox.curselection()) # curselection : 현재 선택된 요소의 인덱스 값 반환

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림
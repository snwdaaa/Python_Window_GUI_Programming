# tkinter -> 윈도우 모듈
from tkinter import *
import tkinter.ttk as ttk # 콤보 박스는 tikinter.ttk에 있다. as를 통해 원하는 이름으로 사용 가능

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 콤보 박스 : 새로운 창을 띄운 후, 여러 항목 중에서 하나를 선택

# values : 여러 항목이 들어있는 리스트
values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 숫자 반환
combobox = ttk.Combobox(root, height=5, values=values) # 콤보 박스 선언
combobox.pack()
combobox.set("카드 결제일") # 최초 목록의 제목 & 버튼 클릭을 통한 값 설정 가능

# 콤보 박스에 입력 막기
# state="readonly" : 읽기 전용이 됨 (선택만 할 수 있움)
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 콤보 박스 선언
readonly_combobox.current(0) # 0번째 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 현재 선택된 값을 출력
    print(readonly_combobox.get())

btn1 = Button(root, text="선택", command=btncmd)
btn1.pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림
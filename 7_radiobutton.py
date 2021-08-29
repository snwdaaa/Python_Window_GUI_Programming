# tkinter -> 윈도우 모듈
from tkinter import *

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 라디오 버튼 (여러 개중에 택 1)

Label(root, text="메뉴를 선택하세요").pack()

# value
# variable : 라디오 버튼의 경우는 여러 개중에서 하나를 선택하는 것이기 떄문에
# 같은 영역에 있는 라디오 버튼들은 하나의 변수로 묶여있어야 한다. (중요)
burger_var = IntVar() # Int형으로 값 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 서로 다른 그룹의 라디오 버튼

Label(root, text="음료를 선택하세요").pack()

beverage_var = StringVar()
btn_beverage1 = Radiobutton(root, text="콜라", value="콜라", variable=beverage_var)
btn_beverage1.select() # 기본값 선택
btn_beverage2 = Radiobutton(root, text="사이다", value="사이다", variable=beverage_var)
btn_beverage3 = Radiobutton(root, text="우유", value="우유", variable=beverage_var)

btn_beverage1.pack()
btn_beverage2.pack()
btn_beverage3.pack()

def btncmd():
    # 라디오 버튼에서 선택된 값 가져오기
    # get 할 때는 각각의 라디오 버튼 변수가 아닌, 라디오 버튼 전체를 관리하는 변수로 가져옴
    print(burger_var.get()) # 해당 변수에서 선택된 라디오 항목의 value를 리턴
    print(beverage_var.get())

btn1 = Button(root, text="주문", command=btncmd)
btn1.pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림